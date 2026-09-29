# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 10:50 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 28 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 29 | 28 | 11 (39%) | 38¢ | 46% | -$0.54 | -0% |
| Silver | 14 | 14 | 4 (29%) | 32¢ | 40% | -$6.72 | -14% |
| Gold | 15 | 14 | 7 (50%) | 44¢ | 52% | $6.18 | +10% |

*Earlier half $16.17 / later half -$16.71.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 28 | 9 (32%) | -$27.67 | -24% |
| 4¢+ ← live bot | 27 | 9 (33%) | -$6.64 | -7% |
| 6¢+ | 27 | 8 (30%) | -$2.36 | -3% |
| 8¢+ | 25 | 8 (32%) | $10.77 | +16% |
| 10¢+ | 23 | 5 (22%) | -$1.39 | -3% |
| 15¢+ | 11 | 4 (36%) | $16.37 | +69% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 697 | -5.3% |
| Hyperliquid price vs Kalshi's target | 697 | -16.2% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:47:04 PM | Gold | UP | 12.9 min | 52¢ | 59% | 5¢ | Open | — |
| 9/28 10:31:35 PM | Silver | DOWN | 13.4 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 10:31:31 PM | Gold | UP | 13.5 min | 59¢ | 68% | 7¢ | ❌ Lost | -$6.07 |
| 9/28 10:16:38 PM | Silver | DOWN | 13.4 min | 40¢ | 51% | 9¢ | ❌ Lost | -$4.17 |
| 9/28 10:16:04 PM | Gold | UP | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/28 10:01:37 PM | Silver | UP | 13.4 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 10:01:05 PM | Gold | UP | 13.9 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 9:51:10 PM | Silver | UP | 8.8 min | 31¢ | 41% | 9¢ | ❌ Lost | -$3.25 |
| 9/28 9:46:04 PM | Gold | DOWN | 13.9 min | 59¢ | 66% | 5¢ | ✅ Won | $3.93 |
| 9/28 9:32:24 PM | Silver | DOWN | 12.6 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 9:32:08 PM | Gold | UP | 12.8 min | 42¢ | 52% | 8¢ | ❌ Lost | -$4.38 |
| 9/28 9:18:13 PM | Gold | DOWN | 11.8 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
