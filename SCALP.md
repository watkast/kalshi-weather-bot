# Range-Scalp Bot

*Updated Sat Oct 17 06:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20527 | 17855 | 2672 (29) | 0 | $-6066.16 | -4.7% |
| **+10¢** | 15465 | 12386 | 3079 (41) | 0 | $-5373.68 | -5.5% |
| **+15¢** | 12933 | 9622 | 3311 (60) | 0 | $-4838.06 | -6.0% |
| **+20¢** | 11462 | 7992 | 3470 (79) | 0 | $-4300.55 | -6.0% |
| **+10¢ (15¢ stop)** | 25220 | 25170 | 50 (29) | 0 | $-9526.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 06:28 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 10-17 06:28 | +10 stop | DOGE | UP | 0.70 | 0.54 | -1.95 |
| 10-17 06:28 | +10 stop | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-17 06:28 | +20 | SOL | DOWN | 0.55 | 0.93 | 3.60 |
| 10-17 06:28 | +15 | SOL | DOWN | 0.55 | 0.93 | 3.60 |
| 10-17 06:28 | +10 | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-17 06:28 | +5 | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-17 06:27 | +10 stop | DOGE | DOWN | 0.66 | 0.39 | -3.03 |
| 10-17 06:26 | +10 stop | DOGE | DOWN | 0.52 | 0.66 | 1.04 |
| 10-17 06:26 | +10 stop | HYPE | DOWN | 0.37 | 0.62 | 2.16 |
| 10-17 06:26 | +10 stop | BTC | DOWN | 0.71 | 0.45 | -2.93 |
| 10-17 06:26 | +10 stop | HYPE | UP | 0.70 | 0.51 | -2.24 |
| 10-17 06:26 | +10 stop | ETH | UP | 0.71 | 0.52 | -2.23 |
| 10-17 06:25 | +10 stop | ETH | DOWN | 0.62 | 0.33 | -3.23 |
| 10-17 06:25 | +20 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-17 06:25 | +15 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-17 06:25 | +10 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-17 06:25 | +5 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-17 06:24 | +10 stop | DOGE | DOWN | 0.68 | 0.42 | -2.94 |
| 10-17 06:24 | +10 stop | NEAR | DOWN | 0.62 | 0.44 | -2.15 |
| 10-17 06:24 | +10 stop | HYPE | DOWN | 0.65 | 0.30 | -3.81 |
| 10-17 06:23 | +10 stop | BTC | UP | 0.58 | 0.28 | -3.33 |
| 10-17 06:23 | +15 | BTC | UP | 0.58 | 0.80 | 1.90 |
| 10-17 06:23 | +10 | BTC | UP | 0.58 | 0.80 | 1.90 |
| 10-17 06:23 | +10 stop | BNB | DOWN | 0.65 | 0.92 | 2.47 |
| 10-17 06:23 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-17 06:23 | +15 | SOL | DOWN | 0.68 | 0.86 | 1.55 |
| 10-17 06:23 | +10 | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-17 06:23 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 10-17 06:22 | +10 stop | DOGE | UP | 0.60 | 0.72 | 0.88 |
| 10-17 06:22 | +10 | DOGE | UP | 0.64 | no | -6.57 |
| 10-17 06:22 | +5 | DOGE | UP | 0.70 | no | -7.15 |
| 10-17 06:22 | +10 stop | NEAR | UP | 0.63 | 0.32 | -3.43 |
| 10-17 06:22 | +5 | SOL | DOWN | 0.69 | 0.77 | 0.52 |
| 10-17 06:21 | +10 stop | ZEC | UP | 0.64 | 0.48 | -1.95 |
| 10-17 06:21 | +10 stop | BNB | UP | 0.55 | 0.39 | -1.95 |
| 10-17 06:21 | +10 stop | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-17 06:21 | +15 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-17 06:21 | +10 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-17 06:21 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
