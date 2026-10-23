# Range-Scalp Bot

*Updated Fri Oct 23 14:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30474 | 26544 | 3930 (39) | 0 | $-8890.94 | -4.6% |
| **+10¢** | 22813 | 18268 | 4545 (56) | 0 | $-7953.63 | -5.5% |
| **+15¢** | 19092 | 14204 | 4888 (79) | 0 | $-7175.73 | -6.0% |
| **+20¢** | 16906 | 11785 | 5121 (102) | 0 | $-6452.55 | -6.1% |
| **+10¢ (15¢ stop)** | 37347 | 37288 | 59 (32) | 0 | $-14114.72 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 14:25 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.95 |
| 10-23 14:25 | +20 | HYPE | DOWN | 0.63 | 0.92 | 2.67 |
| 10-23 14:25 | +15 | HYPE | DOWN | 0.63 | 0.92 | 2.67 |
| 10-23 14:25 | +10 | HYPE | DOWN | 0.63 | 0.92 | 2.67 |
| 10-23 14:25 | +5 | HYPE | DOWN | 0.63 | 0.92 | 2.67 |
| 10-23 14:16 | +10 stop | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-23 14:16 | +20 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-23 14:16 | +15 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-23 14:16 | +10 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-23 14:16 | +5 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 10-23 14:15 | +10 stop | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 14:15 | +20 | NEAR | DOWN | 0.59 | 0.88 | 2.65 |
| 10-23 14:15 | +15 | NEAR | DOWN | 0.59 | 0.88 | 2.65 |
| 10-23 14:15 | +10 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 14:15 | +5 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 14:09 | +10 stop | ZEC | UP | 0.70 | 0.48 | -2.53 |
| 10-23 14:09 | +15 | ZEC | UP | 0.70 | no | -7.11 |
| 10-23 14:09 | +10 | ZEC | UP | 0.69 | no | -7.05 |
| 10-23 14:09 | +5 | ZEC | UP | 0.69 | no | -7.05 |
| 10-23 14:08 | +10 stop | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-23 14:07 | +10 stop | BNB | DOWN | 0.54 | 0.73 | 1.58 |
| 10-23 14:07 | +5 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-23 14:06 | +5 | ZEC | UP | 0.55 | 0.62 | 0.36 |
| 10-23 14:05 | +5 | ZEC | UP | 0.60 | 0.65 | 0.18 |
| 10-23 14:05 | +10 stop | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-23 14:05 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 14:05 | +10 stop | SOL | DOWN | 0.64 | 0.47 | -2.00 |
| 10-23 14:04 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-23 14:04 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-23 14:04 | +10 stop | XRP | UP | 0.54 | 0.37 | -2.05 |
| 10-23 14:04 | +10 stop | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 10-23 14:04 | +20 | ZEC | UP | 0.62 | no | -6.37 |
| 10-23 14:04 | +15 | ZEC | UP | 0.62 | 0.81 | 1.62 |
| 10-23 14:04 | +10 | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 10-23 14:04 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 10-23 14:04 | +10 stop | HYPE | UP | 0.52 | 0.35 | -2.08 |
| 10-23 14:03 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-23 14:03 | +20 | BTC | DOWN | 0.59 | 0.80 | 1.81 |
| 10-23 14:03 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-23 14:03 | +10 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
