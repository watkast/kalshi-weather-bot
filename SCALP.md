# Range-Scalp Bot

*Updated Fri Oct 23 00:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29516 | 25693 | 3823 (39) | 5 | $-8698.55 | -4.7% |
| **+10¢** | 22128 | 17702 | 4426 (55) | 7 | $-7834.05 | -5.6% |
| **+15¢** | 18525 | 13774 | 4751 (78) | 9 | $-7006.15 | -6.0% |
| **+20¢** | 16393 | 11413 | 4980 (100) | 9 | $-6347.37 | -6.2% |
| **+10¢ (15¢ stop)** | 36239 | 36180 | 59 (32) | 3 | $-13688.81 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 00:23 | +10 stop | XRP | DOWN | 0.38 | 0.57 | 1.55 |
| 10-23 00:23 | +5 | XRP | DOWN | 0.38 | 0.57 | 1.55 |
| 10-23 00:23 | +10 stop | BTC | DOWN | 0.53 | open |  |
| 10-23 00:23 | +5 | BTC | DOWN | 0.53 | 0.62 | 0.55 |
| 10-23 00:22 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-23 00:22 | +10 stop | ZEC | DOWN | 0.53 | open |  |
| 10-23 00:22 | +10 stop | NEAR | DOWN | 0.62 | 0.47 | -1.85 |
| 10-23 00:22 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-23 00:22 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-23 00:22 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-23 00:22 | +20 | SOL | UP | 0.71 | open |  |
| 10-23 00:22 | +15 | SOL | UP | 0.71 | open |  |
| 10-23 00:22 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-23 00:22 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-23 00:22 | +10 stop | DOGE | DOWN | 0.67 | 0.41 | -2.93 |
| 10-23 00:22 | +10 stop | XRP | DOWN | 0.64 | 0.77 | 0.98 |
| 10-23 00:22 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 10-23 00:22 | +10 | BNB | UP | 0.64 | open |  |
| 10-23 00:22 | +5 | BNB | UP | 0.64 | open |  |
| 10-23 00:21 | +10 stop | HYPE | UP | 0.68 | open |  |
| 10-23 00:21 | +5 | HYPE | UP | 0.68 | open |  |
| 10-23 00:21 | +10 stop | ETH | UP | 0.58 | 0.42 | -1.96 |
| 10-23 00:21 | +10 stop | BTC | UP | 0.65 | 0.50 | -1.84 |
| 10-23 00:21 | +10 stop | ZEC | UP | 0.66 | 0.50 | -1.94 |
| 10-23 00:21 | +10 | ZEC | UP | 0.66 | open |  |
| 10-23 00:21 | +5 | ZEC | UP | 0.66 | open |  |
| 10-23 00:21 | +10 stop | XRP | UP | 0.67 | 0.45 | -2.54 |
| 10-23 00:20 | +10 stop | BTC | UP | 0.54 | 0.64 | 0.65 |
| 10-23 00:20 | +10 stop | NEAR | UP | 0.70 | 0.32 | -4.11 |
| 10-23 00:20 | +10 stop | HYPE | DOWN | 0.43 | 0.54 | 0.70 |
| 10-23 00:20 | +20 | HYPE | DOWN | 0.43 | open |  |
| 10-23 00:20 | +15 | HYPE | DOWN | 0.43 | open |  |
| 10-23 00:20 | +10 | HYPE | DOWN | 0.44 | open |  |
| 10-23 00:20 | +5 | HYPE | DOWN | 0.44 | 0.54 | 0.60 |
| 10-23 00:19 | +5 | SOL | UP | 0.66 | 0.72 | 0.29 |
| 10-23 00:19 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 10-23 00:19 | +10 stop | BNB | UP | 0.68 | 0.79 | 0.82 |
| 10-23 00:19 | +20 | BNB | UP | 0.68 | open |  |
| 10-23 00:19 | +15 | BNB | UP | 0.68 | open |  |
| 10-23 00:19 | +10 | BNB | UP | 0.68 | 0.79 | 0.82 |
