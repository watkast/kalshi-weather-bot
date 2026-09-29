# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 11:51 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 38 | 36 | 14 (39%) | 42¢ | 50% | -$15.29 | -10% |
| Silver | 19 | 18 | 6 (33%) | 35¢ | 44% | -$5.81 | -9% |
| Gold | 19 | 18 | 8 (44%) | 48¢ | 56% | -$9.48 | -11% |

*Earlier half $21.52 / later half -$36.81.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 36 | 11 (31%) | -$50.19 | -31% |
| 4¢+ ← live bot | 35 | 12 (34%) | -$13.23 | -10% |
| 6¢+ | 33 | 11 (33%) | $0.49 | +0% |
| 8¢+ | 30 | 11 (37%) | $22.27 | +25% |
| 10¢+ | 26 | 7 (27%) | $2.33 | +3% |
| 15¢+ | 12 | 4 (33%) | $13.32 | +50% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 897 | -5.2% |
| Hyperliquid price vs Kalshi's target | 897 | -13.8% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:46:05 PM | Gold | UP | 13.9 min | 28¢ | 34% | 5¢ | Open | — |
| 9/28 11:46:05 PM | Silver | UP | 13.9 min | 33¢ | 42% | 8¢ | Open | — |
| 9/28 11:34:38 PM | Silver | DOWN | 10.4 min | 81¢ | 92% | 10¢ | ❌ Lost | -$8.21 |
| 9/28 11:31:34 PM | Gold | DOWN | 13.4 min | 75¢ | 83% | 6¢ | ❌ Lost | -$7.64 |
| 9/28 11:18:01 PM | Silver | DOWN | 12.0 min | 28¢ | 46% | 16¢ | ✅ Won | $7.05 |
| 9/28 11:17:37 PM | Gold | DOWN | 12.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/28 11:02:38 PM | Gold | UP | 12.4 min | 65¢ | 73% | 7¢ | ✅ Won | $3.34 |
| 9/28 11:01:02 PM | Silver | DOWN | 13.9 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 10:52:13 PM | Silver | DOWN | 7.8 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 10:47:04 PM | Gold | UP | 12.9 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.38 |
| 9/28 10:31:35 PM | Silver | DOWN | 13.4 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 10:31:31 PM | Gold | UP | 13.5 min | 59¢ | 68% | 7¢ | ❌ Lost | -$6.07 |
