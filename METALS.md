# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 10:30 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 26 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 26 | 26 | 11 (42%) | 37¢ | 45% | $8.27 | +8% |
| Silver | 13 | 13 | 4 (31%) | 32¢ | 40% | -$3.98 | -9% |
| Gold | 13 | 13 | 7 (54%) | 43¢ | 50% | $12.25 | +21% |

*Earlier half $11.35 / later half -$3.08.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 26 | 9 (35%) | -$20.55 | -19% |
| 4¢+ ← live bot | 25 | 9 (36%) | -$3.34 | -4% |
| 6¢+ | 25 | 8 (32%) | $0.84 | +1% |
| 8¢+ | 24 | 8 (33%) | $13.20 | +20% |
| 10¢+ | 22 | 5 (23%) | -$0.81 | -2% |
| 15¢+ | 11 | 4 (36%) | $16.37 | +69% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 647 | -5.1% |
| Hyperliquid price vs Kalshi's target | 647 | -15.3% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:16:38 PM | Silver | DOWN | 13.4 min | 40¢ | 51% | 9¢ | ❌ Lost | -$4.17 |
| 9/28 10:16:04 PM | Gold | UP | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/28 10:01:37 PM | Silver | UP | 13.4 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 10:01:05 PM | Gold | UP | 13.9 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 9:51:10 PM | Silver | UP | 8.8 min | 31¢ | 41% | 9¢ | ❌ Lost | -$3.25 |
| 9/28 9:46:04 PM | Gold | DOWN | 13.9 min | 59¢ | 66% | 5¢ | ✅ Won | $3.93 |
| 9/28 9:32:24 PM | Silver | DOWN | 12.6 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 9:32:08 PM | Gold | UP | 12.8 min | 42¢ | 52% | 8¢ | ❌ Lost | -$4.38 |
| 9/28 9:18:13 PM | Gold | DOWN | 11.8 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 9:16:07 PM | Silver | DOWN | 13.9 min | 29¢ | 37% | 6¢ | ❌ Lost | -$3.05 |
| 9/28 9:02:38 PM | Silver | DOWN | 12.4 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 9:01:26 PM | Gold | DOWN | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
