# Range-Scalp Bot

*Updated Sun Nov 15 14:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60876 | 53113 | 7763 (112) | 0 | $-16454.17 | -4.3% |
| **+10¢** | 45482 | 36381 | 9101 (150) | 0 | $-15505.66 | -5.4% |
| **+15¢** | 38088 | 28273 | 9815 (188) | 0 | $-14175.88 | -5.9% |
| **+20¢** | 33944 | 23649 | 10295 (240) | 0 | $-12458.83 | -5.9% |
| **+10¢ (15¢ stop)** | 74087 | 73936 | 151 (89) | 0 | $-27236.00 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 13:58 | +5 | HYPE | UP | 0.52 | 0.66 | 1.06 |
| 11-15 13:58 | +10 stop | HYPE | DOWN | 0.50 | 0.33 | -2.03 |
| 11-15 13:58 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 11-15 13:56 | +10 stop | DOGE | DOWN | 0.56 | 0.73 | 1.40 |
| 11-15 13:56 | +10 stop | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 11-15 13:56 | +10 | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 11-15 13:56 | +5 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-15 13:56 | +10 stop | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 11-15 13:56 | +10 | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 11-15 13:55 | +10 stop | ZEC | UP | 0.59 | 0.13 | -4.83 |
| 11-15 13:55 | +10 stop | XRP | DOWN | 0.58 | 0.72 | 1.07 |
| 11-15 13:55 | +15 | XRP | DOWN | 0.58 | 0.83 | 2.22 |
| 11-15 13:55 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 11-15 13:54 | +10 stop | ZEC | UP | 0.60 | 0.76 | 1.30 |
| 11-15 13:54 | +10 stop | SOL | UP | 0.57 | 0.36 | -2.45 |
| 11-15 13:54 | +10 | BTC | DOWN | 0.49 | 0.66 | 1.36 |
| 11-15 13:54 | +5 | BTC | DOWN | 0.49 | 0.58 | 0.54 |
| 11-15 13:54 | +10 stop | BTC | DOWN | 0.54 | 0.66 | 0.86 |
| 11-15 13:53 | +10 stop | SOL | UP | 0.46 | 0.66 | 1.66 |
| 11-15 13:53 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 13:53 | +10 stop | DOGE | UP | 0.59 | 0.38 | -2.44 |
| 11-15 13:52 | +10 stop | BTC | UP | 0.66 | 0.44 | -2.54 |
| 11-15 13:52 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 13:52 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 13:52 | +5 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 13:51 | +10 stop | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 11-15 13:51 | +10 stop | XRP | UP | 0.61 | 0.44 | -2.10 |
| 11-15 13:51 | +5 | XRP | UP | 0.58 | no | -5.98 |
| 11-15 13:51 | +10 stop | ZEC | UP | 0.68 | 0.53 | -1.85 |
| 11-15 13:51 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-15 13:51 | +5 | XRP | DOWN | 0.57 | 0.62 | 0.15 |
| 11-15 13:50 | +10 stop | XRP | DOWN | 0.56 | 0.40 | -1.95 |
| 11-15 13:50 | +10 | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 11-15 13:50 | +5 | XRP | DOWN | 0.56 | 0.64 | 0.45 |
| 11-15 13:49 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-15 13:49 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.89 |
| 11-15 13:49 | +10 stop | ETH | UP | 0.63 | 0.78 | 1.20 |
| 11-15 13:49 | +10 stop | BNB | UP | 0.63 | 0.78 | 1.20 |
| 11-15 13:49 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-15 13:49 | +20 | NEAR | DOWN | 0.64 | 0.84 | 1.73 |
