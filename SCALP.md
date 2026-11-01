# Range-Scalp Bot

*Updated Sun Nov 01 12:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43605 | 37996 | 5609 (63) | 1 | $-12454.71 | -4.5% |
| **+10¢** | 32532 | 26055 | 6477 (85) | 1 | $-11157.11 | -5.5% |
| **+15¢** | 27230 | 20254 | 6976 (112) | 1 | $-10188.12 | -6.0% |
| **+20¢** | 24180 | 16872 | 7308 (146) | 1 | $-9001.25 | -5.9% |
| **+10¢ (15¢ stop)** | 53200 | 53115 | 85 (50) | 1 | $-20112.74 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 12:23 | +5 | HYPE | UP | 0.67 | open |  |
| 11-01 12:22 | +10 stop | HYPE | UP | 0.69 | open |  |
| 11-01 12:22 | +5 | HYPE | UP | 0.59 | 0.66 | 0.37 |
| 11-01 12:21 | +10 stop | HYPE | DOWN | 0.60 | 0.34 | -2.94 |
| 11-01 12:21 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-01 12:21 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-01 12:21 | +10 | HYPE | DOWN | 0.57 | open |  |
| 11-01 12:21 | +5 | HYPE | DOWN | 0.57 | 0.65 | 0.46 |
| 11-01 12:20 | +10 stop | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 11-01 12:20 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 11-01 12:19 | +10 stop | BNB | DOWN | 0.53 | 0.64 | 0.75 |
| 11-01 12:19 | +10 | BNB | DOWN | 0.55 | 0.66 | 0.72 |
| 11-01 12:19 | +5 | BNB | DOWN | 0.56 | 0.64 | 0.45 |
| 11-01 12:17 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.67 |
| 11-01 12:17 | +20 | BNB | DOWN | 0.57 | 0.77 | 1.69 |
| 11-01 12:17 | +15 | BNB | DOWN | 0.58 | 0.77 | 1.60 |
| 11-01 12:17 | +10 | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-01 12:17 | +5 | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-01 12:14 | +10 stop | BTC | UP | 0.59 | 0.70 | 0.78 |
| 11-01 12:14 | +10 | BTC | UP | 0.59 | 0.70 | 0.78 |
| 11-01 12:14 | +5 | BTC | UP | 0.58 | 0.67 | 0.56 |
| 11-01 12:13 | +5 | BNB | DOWN | 0.68 | 0.94 | 2.44 |
| 11-01 12:12 | +10 stop | DOGE | UP | 0.67 | 0.84 | 1.44 |
| 11-01 12:12 | +20 | DOGE | UP | 0.67 | 0.97 | 2.80 |
| 11-01 12:12 | +15 | DOGE | UP | 0.67 | 0.84 | 1.44 |
| 11-01 12:12 | +10 | DOGE | UP | 0.67 | 0.84 | 1.44 |
| 11-01 12:12 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 11-01 12:12 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.76 |
| 11-01 12:12 | +20 | BNB | DOWN | 0.56 | 0.94 | 3.62 |
| 11-01 12:12 | +15 | BNB | DOWN | 0.57 | 0.94 | 3.52 |
| 11-01 12:12 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 11-01 12:12 | +5 | BNB | DOWN | 0.57 | 0.65 | 0.47 |
| 11-01 12:12 | +10 stop | BTC | DOWN | 0.49 | 0.62 | 0.91 |
| 11-01 12:12 | +20 | BTC | DOWN | 0.49 | yes | -5.08 |
| 11-01 12:12 | +15 | BTC | DOWN | 0.49 | yes | -5.08 |
| 11-01 12:12 | +10 | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-01 12:12 | +5 | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-01 12:11 | +10 stop | SOL | DOWN | 0.70 | 0.88 | 1.57 |
| 11-01 12:11 | +10 stop | NEAR | DOWN | 0.63 | 0.83 | 1.69 |
| 11-01 12:10 | +10 stop | SOL | UP | 0.62 | 0.43 | -2.25 |
