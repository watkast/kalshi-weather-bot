# Range-Scalp Bot

*Updated Sun Oct 18 12:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22573 | 19649 | 2924 (29) | 0 | $-6595.41 | -4.6% |
| **+10¢** | 16983 | 13605 | 3378 (43) | 0 | $-5871.95 | -5.5% |
| **+15¢** | 14220 | 10574 | 3646 (64) | 0 | $-5370.00 | -6.0% |
| **+20¢** | 12587 | 8770 | 3817 (82) | 0 | $-4787.99 | -6.1% |
| **+10¢ (15¢ stop)** | 27754 | 27704 | 50 (29) | 0 | $-10588.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 12:31 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-18 12:31 | +20 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-18 12:31 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-18 12:31 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-18 12:31 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 12:29 | +10 stop | NEAR | UP | 0.48 | 0.58 | 0.64 |
| 10-18 12:29 | +20 | NEAR | UP | 0.41 | yes | 5.73 |
| 10-18 12:29 | +15 | NEAR | UP | 0.45 | yes | 5.32 |
| 10-18 12:29 | +10 | NEAR | UP | 0.40 | 0.58 | 1.45 |
| 10-18 12:29 | +5 | NEAR | UP | 0.42 | 0.58 | 1.21 |
| 10-18 12:27 | +10 stop | NEAR | DOWN | 0.20 | 0.53 | 3.00 |
| 10-18 12:27 | +10 | NEAR | DOWN | 0.21 | 0.53 | 2.90 |
| 10-18 12:27 | +5 | NEAR | DOWN | 0.21 | 0.53 | 2.90 |
| 10-18 12:27 | +10 | NEAR | UP | 0.40 | 0.57 | 1.35 |
| 10-18 12:27 | +5 | NEAR | UP | 0.40 | 0.57 | 1.35 |
| 10-18 12:26 | +10 stop | SOL | UP | 0.63 | 0.81 | 1.52 |
| 10-18 12:26 | +10 stop | XRP | UP | 0.58 | 0.84 | 2.32 |
| 10-18 12:26 | +10 stop | BNB | UP | 0.59 | 0.83 | 2.13 |
| 10-18 12:25 | +10 stop | NEAR | UP | 0.63 | 0.32 | -3.43 |
| 10-18 12:25 | +20 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 10-18 12:25 | +15 | NEAR | UP | 0.58 | 0.79 | 1.80 |
| 10-18 12:25 | +10 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-18 12:25 | +5 | NEAR | UP | 0.58 | 0.68 | 0.66 |
| 10-18 12:24 | +10 stop | SOL | UP | 0.67 | 0.48 | -2.24 |
| 10-18 12:24 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-18 12:24 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-18 12:24 | +10 stop | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 10-18 12:23 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 10-18 12:23 | +10 stop | SOL | DOWN | 0.61 | 0.45 | -1.95 |
| 10-18 12:23 | +5 | SOL | DOWN | 0.61 | yes | -6.27 |
| 10-18 12:22 | +15 | DOGE | UP | 0.60 | 0.83 | 2.03 |
| 10-18 12:22 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 10-18 12:22 | +10 stop | NEAR | DOWN | 0.56 | 0.37 | -2.25 |
| 10-18 12:21 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 10-18 12:21 | +10 stop | NEAR | UP | 0.51 | 0.36 | -1.85 |
| 10-18 12:21 | +10 stop | DOGE | UP | 0.66 | 0.83 | 1.44 |
| 10-18 12:21 | +10 stop | BNB | UP | 0.60 | 0.30 | -3.32 |
| 10-18 12:20 | +10 stop | XRP | UP | 0.65 | 0.43 | -2.54 |
| 10-18 12:20 | +10 stop | BNB | UP | 0.64 | 0.46 | -2.15 |
| 10-18 12:20 | +10 | BNB | UP | 0.64 | 0.83 | 1.63 |
