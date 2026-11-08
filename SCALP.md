# Range-Scalp Bot

*Updated Sun Nov 08 03:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51889 | 45244 | 6645 (80) | 0 | $-14395.11 | -4.4% |
| **+10¢** | 38726 | 30974 | 7752 (106) | 0 | $-13425.81 | -5.5% |
| **+15¢** | 32430 | 24076 | 8354 (135) | 0 | $-12316.55 | -6.1% |
| **+20¢** | 28853 | 20096 | 8757 (180) | 0 | $-10838.64 | -6.0% |
| **+10¢ (15¢ stop)** | 63194 | 63091 | 103 (61) | 0 | $-23412.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 03:01 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-08 03:01 | +20 | BTC | UP | 0.68 | 0.89 | 1.87 |
| 11-08 03:01 | +15 | BTC | UP | 0.68 | 0.83 | 1.24 |
| 11-08 03:01 | +10 | BTC | UP | 0.68 | 0.78 | 0.71 |
| 11-08 03:01 | +5 | BTC | UP | 0.68 | 0.75 | 0.40 |
| 11-08 02:56 | +10 stop | BNB | DOWN | 0.57 | 0.05 | -5.40 |
| 11-08 02:55 | +10 stop | HYPE | UP | 0.55 | 0.76 | 1.76 |
| 11-08 02:55 | +5 | HYPE | UP | 0.55 | 0.61 | 0.22 |
| 11-08 02:54 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.90 |
| 11-08 02:53 | +10 stop | BNB | UP | 0.64 | 0.47 | -2.05 |
| 11-08 02:52 | +5 | HYPE | DOWN | 0.48 | 0.65 | 1.36 |
| 11-08 02:52 | +10 stop | XRP | DOWN | 0.59 | 0.37 | -2.54 |
| 11-08 02:52 | +15 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-08 02:52 | +10 stop | SOL | UP | 0.70 | 0.86 | 1.36 |
| 11-08 02:51 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 11-08 02:51 | +10 stop | BTC | UP | 0.57 | 0.74 | 1.38 |
| 11-08 02:51 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-08 02:50 | +10 stop | NEAR | DOWN | 0.66 | 0.46 | -2.34 |
| 11-08 02:49 | +5 | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 11-08 02:48 | +10 stop | XRP | DOWN | 0.58 | 0.68 | 0.66 |
| 11-08 02:48 | +10 stop | SOL | DOWN | 0.57 | 0.39 | -2.15 |
| 11-08 02:48 | +10 stop | ZEC | UP | 0.61 | 0.73 | 0.89 |
| 11-08 02:48 | +20 | ZEC | UP | 0.61 | 0.83 | 1.93 |
| 11-08 02:48 | +15 | ZEC | UP | 0.61 | 0.83 | 1.93 |
| 11-08 02:48 | +10 | ZEC | UP | 0.61 | 0.73 | 0.89 |
| 11-08 02:48 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 11-08 02:47 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.15 |
| 11-08 02:47 | +20 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-08 02:47 | +15 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-08 02:47 | +10 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-08 02:47 | +5 | BNB | DOWN | 0.58 | yes | -5.98 |
| 11-08 02:47 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.85 |
| 11-08 02:47 | +10 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-08 02:47 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-08 02:47 | +20 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-08 02:47 | +15 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-08 02:47 | +10 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-08 02:47 | +5 | SOL | DOWN | 0.67 | yes | -6.86 |
| 11-08 02:47 | +10 stop | BTC | DOWN | 0.61 | 0.43 | -2.15 |
| 11-08 02:47 | +20 | BTC | DOWN | 0.61 | yes | -6.27 |
