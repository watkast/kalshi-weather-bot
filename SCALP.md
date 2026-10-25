# Range-Scalp Bot

*Updated Sun Oct 25 18:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33546 | 29274 | 4272 (43) | 4 | $-9382.28 | -4.4% |
| **+10¢** | 25111 | 20166 | 4945 (65) | 4 | $-8297.44 | -5.3% |
| **+15¢** | 21002 | 15680 | 5322 (89) | 5 | $-7437.63 | -5.6% |
| **+20¢** | 18613 | 13041 | 5572 (111) | 5 | $-6535.11 | -5.6% |
| **+10¢ (15¢ stop)** | 41117 | 41055 | 62 (33) | 0 | $-15683.80 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 18:29 | +10 stop | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-25 18:29 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-25 18:29 | +10 | ETH | DOWN | 0.69 | 0.83 | 1.15 |
| 10-25 18:28 | +10 stop | ZEC | DOWN | 0.53 | 0.66 | 0.94 |
| 10-25 18:28 | +10 stop | ZEC | UP | 0.63 | 0.39 | -2.74 |
| 10-25 18:28 | +20 | ZEC | UP | 0.63 | open |  |
| 10-25 18:28 | +15 | ZEC | UP | 0.63 | open |  |
| 10-25 18:28 | +10 | ZEC | UP | 0.63 | open |  |
| 10-25 18:28 | +5 | ZEC | UP | 0.62 | open |  |
| 10-25 18:27 | +10 stop | ETH | UP | 0.66 | 0.39 | -3.03 |
| 10-25 18:26 | +10 stop | ETH | DOWN | 0.54 | 0.35 | -2.24 |
| 10-25 18:26 | +5 | ETH | DOWN | 0.54 | 0.62 | 0.45 |
| 10-25 18:26 | +10 stop | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-25 18:26 | +15 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-25 18:26 | +10 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-25 18:26 | +5 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 10-25 18:25 | +10 stop | ETH | UP | 0.56 | 0.39 | -2.05 |
| 10-25 18:25 | +20 | ETH | UP | 0.56 | 0.92 | 3.36 |
| 10-25 18:25 | +15 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 10-25 18:25 | +10 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 10-25 18:25 | +5 | ETH | UP | 0.56 | 0.65 | 0.56 |
| 10-25 18:24 | +10 stop | BTC | UP | 0.64 | 0.22 | -4.50 |
| 10-25 18:24 | +20 | BTC | UP | 0.64 | open |  |
| 10-25 18:24 | +15 | BTC | UP | 0.63 | open |  |
| 10-25 18:24 | +10 | BTC | UP | 0.66 | open |  |
| 10-25 18:24 | +5 | BTC | UP | 0.66 | open |  |
| 10-25 18:24 | +10 stop | HYPE | UP | 0.56 | 0.38 | -2.15 |
| 10-25 18:22 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-25 18:20 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 10-25 18:18 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-25 18:18 | +10 | BTC | UP | 0.71 | 0.82 | 0.84 |
| 10-25 18:18 | +5 | BTC | UP | 0.71 | 0.79 | 0.53 |
| 10-25 18:18 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-25 18:18 | +10 | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-25 18:18 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-25 18:17 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-25 18:17 | +20 | ETH | UP | 0.60 | 0.80 | 1.71 |
| 10-25 18:17 | +15 | ETH | UP | 0.60 | 0.75 | 1.19 |
| 10-25 18:17 | +10 | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-25 18:17 | +5 | ETH | UP | 0.60 | 0.71 | 0.78 |
