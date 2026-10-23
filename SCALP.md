# Range-Scalp Bot

*Updated Fri Oct 23 18:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30761 | 26798 | 3963 (39) | 0 | $-8961.14 | -4.6% |
| **+10¢** | 23018 | 18439 | 4579 (56) | 0 | $-7980.73 | -5.5% |
| **+15¢** | 19258 | 14328 | 4930 (79) | 0 | $-7231.61 | -6.0% |
| **+20¢** | 17056 | 11895 | 5161 (102) | 0 | $-6466.34 | -6.0% |
| **+10¢ (15¢ stop)** | 37744 | 37685 | 59 (32) | 0 | $-14378.13 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 18:27 | +10 stop | XRP | DOWN | 0.53 | 0.68 | 1.16 |
| 10-23 18:26 | +10 stop | BNB | DOWN | 0.65 | 0.92 | 2.46 |
| 10-23 18:26 | +10 stop | NEAR | UP | 0.67 | 0.30 | -4.01 |
| 10-23 18:25 | +10 stop | HYPE | DOWN | 0.69 | 0.83 | 1.15 |
| 10-23 18:24 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 10-23 18:24 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 18:24 | +10 stop | NEAR | DOWN | 0.58 | 0.41 | -2.05 |
| 10-23 18:24 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 10-23 18:24 | +10 stop | HYPE | UP | 0.55 | 0.32 | -2.64 |
| 10-23 18:24 | +20 | HYPE | UP | 0.55 | no | -5.68 |
| 10-23 18:24 | +15 | HYPE | UP | 0.55 | no | -5.68 |
| 10-23 18:24 | +10 | HYPE | UP | 0.55 | no | -5.68 |
| 10-23 18:24 | +5 | HYPE | UP | 0.55 | no | -5.68 |
| 10-23 18:24 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 18:23 | +10 stop | XRP | UP | 0.52 | 0.63 | 0.73 |
| 10-23 18:23 | +10 stop | DOGE | UP | 0.40 | 0.56 | 1.25 |
| 10-23 18:23 | +10 stop | NEAR | UP | 0.68 | 0.49 | -2.24 |
| 10-23 18:23 | +5 | XRP | UP | 0.65 | no | -6.66 |
| 10-23 18:23 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-23 18:22 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-23 18:22 | +10 stop | BTC | DOWN | 0.60 | 0.77 | 1.40 |
| 10-23 18:22 | +10 stop | XRP | DOWN | 0.54 | 0.35 | -2.24 |
| 10-23 18:22 | +5 | XRP | DOWN | 0.53 | 0.62 | 0.55 |
| 10-23 18:22 | +10 stop | NEAR | DOWN | 0.66 | 0.45 | -2.44 |
| 10-23 18:22 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-23 18:20 | +10 stop | BTC | UP | 0.54 | 0.36 | -2.15 |
| 10-23 18:20 | +10 | BTC | UP | 0.54 | no | -5.58 |
| 10-23 18:20 | +10 stop | NEAR | DOWN | 0.52 | 0.66 | 1.06 |
| 10-23 18:20 | +5 | NEAR | DOWN | 0.53 | 0.66 | 0.96 |
| 10-23 18:20 | +5 | HYPE | UP | 0.60 | 0.68 | 0.47 |
| 10-23 18:20 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 10-23 18:20 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-23 18:20 | +10 stop | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-23 18:20 | +10 stop | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 10-23 18:20 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-23 18:20 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 18:19 | +10 stop | XRP | UP | 0.56 | 0.38 | -2.15 |
| 10-23 18:19 | +15 | XRP | UP | 0.56 | no | -5.78 |
| 10-23 18:19 | +10 | XRP | UP | 0.56 | no | -5.78 |
| 10-23 18:19 | +5 | XRP | UP | 0.56 | 0.61 | 0.15 |
