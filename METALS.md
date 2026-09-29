# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 11:00 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 30 | 30 | 12 (40%) | 39¢ | 46% | -$0.60 | -0% |
| Silver | 15 | 15 | 5 (33%) | 33¢ | 41% | -$1.40 | -3% |
| Gold | 15 | 15 | 7 (47%) | 44¢ | 52% | $0.80 | +1% |

*Earlier half $21.79 / later half -$22.39.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 30 | 9 (30%) | -$36.10 | -29% |
| 4¢+ ← live bot | 29 | 9 (31%) | -$15.07 | -14% |
| 6¢+ | 29 | 8 (28%) | -$10.40 | -12% |
| 8¢+ | 27 | 8 (30%) | $3.36 | +4% |
| 10¢+ | 24 | 5 (21%) | -$4.44 | -8% |
| 15¢+ | 12 | 4 (33%) | $13.32 | +50% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 747 | -5.9% |
| Hyperliquid price vs Kalshi's target | 747 | -25.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:52:13 PM | Silver | DOWN | 7.8 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 10:47:04 PM | Gold | UP | 12.9 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.38 |
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
