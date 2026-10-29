# Range-Scalp Bot

*Updated Thu Oct 29 02:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38817 | 33876 | 4941 (49) | 5 | $-10881.13 | -4.4% |
| **+10¢** | 28955 | 23249 | 5706 (71) | 5 | $-9636.28 | -5.3% |
| **+15¢** | 24223 | 18092 | 6131 (97) | 5 | $-8589.69 | -5.6% |
| **+20¢** | 21491 | 15069 | 6422 (125) | 6 | $-7497.76 | -5.6% |
| **+10¢ (15¢ stop)** | 47480 | 47413 | 67 (35) | 0 | $-18016.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 02:24 | +10 stop | XRP | UP | 0.71 | 0.37 | -3.72 |
| 10-29 02:23 | +10 stop | XRP | DOWN | 0.60 | 0.35 | -2.83 |
| 10-29 02:23 | +5 | XRP | DOWN | 0.60 | 0.82 | 1.92 |
| 10-29 02:22 | +10 stop | BTC | UP | 0.68 | 0.81 | 1.03 |
| 10-29 02:22 | +10 stop | NEAR | UP | 0.61 | 0.81 | 1.72 |
| 10-29 02:22 | +10 stop | BNB | DOWN | 0.50 | 0.20 | -3.34 |
| 10-29 02:21 | +10 stop | ETH | UP | 0.71 | 0.83 | 0.95 |
| 10-29 02:21 | +10 stop | BTC | UP | 0.58 | 0.73 | 1.18 |
| 10-29 02:20 | +10 stop | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-29 02:20 | +10 stop | BNB | DOWN | 0.59 | 0.42 | -2.05 |
| 10-29 02:20 | +10 stop | NEAR | UP | 0.59 | 0.72 | 0.98 |
| 10-29 02:20 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-29 02:20 | +20 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 10-29 02:20 | +15 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 10-29 02:20 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 10-29 02:20 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-29 02:20 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 02:20 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 10-29 02:20 | +10 stop | ETH | UP | 0.59 | 0.69 | 0.68 |
| 10-29 02:20 | +10 stop | SOL | UP | 0.65 | 0.78 | 1.01 |
| 10-29 02:20 | +20 | SOL | UP | 0.65 | 0.86 | 1.85 |
| 10-29 02:20 | +15 | SOL | UP | 0.65 | 0.86 | 1.85 |
| 10-29 02:20 | +10 | SOL | UP | 0.65 | 0.78 | 1.01 |
| 10-29 02:20 | +5 | SOL | UP | 0.65 | 0.72 | 0.39 |
| 10-29 02:19 | +10 stop | HYPE | UP | 0.56 | 0.73 | 1.34 |
| 10-29 02:19 | +10 stop | BNB | UP | 0.52 | 0.37 | -1.85 |
| 10-29 02:19 | +10 stop | XRP | UP | 0.67 | 0.38 | -3.23 |
| 10-29 02:18 | +10 stop | BTC | UP | 0.70 | 0.54 | -1.93 |
| 10-29 02:18 | +10 stop | NEAR | UP | 0.70 | 0.52 | -2.13 |
| 10-29 02:18 | +10 stop | SOL | UP | 0.62 | 0.76 | 1.10 |
| 10-29 02:18 | +20 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 10-29 02:18 | +15 | SOL | UP | 0.62 | 0.80 | 1.51 |
| 10-29 02:18 | +10 | SOL | UP | 0.62 | 0.76 | 1.10 |
| 10-29 02:18 | +5 | SOL | UP | 0.62 | 0.76 | 1.10 |
| 10-29 02:17 | +5 | BNB | DOWN | 0.62 | open |  |
| 10-29 02:17 | +10 stop | HYPE | DOWN | 0.52 | 0.36 | -1.95 |
| 10-29 02:17 | +20 | HYPE | DOWN | 0.52 | open |  |
| 10-29 02:17 | +15 | HYPE | DOWN | 0.52 | open |  |
| 10-29 02:17 | +10 | HYPE | DOWN | 0.52 | open |  |
| 10-29 02:17 | +5 | HYPE | DOWN | 0.52 | open |  |
