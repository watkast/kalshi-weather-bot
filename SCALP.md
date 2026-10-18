# Range-Scalp Bot

*Updated Sun Oct 18 18:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22819 | 19865 | 2954 (29) | 0 | $-6652.42 | -4.6% |
| **+10¢** | 17163 | 13752 | 3411 (43) | 0 | $-5917.86 | -5.5% |
| **+15¢** | 14381 | 10699 | 3682 (64) | 0 | $-5399.46 | -6.0% |
| **+20¢** | 12732 | 8880 | 3852 (82) | 0 | $-4777.13 | -6.0% |
| **+10¢ (15¢ stop)** | 28078 | 28028 | 50 (29) | 0 | $-10740.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 16:57 | +10 stop | BNB | DOWN | 0.50 | 0.75 | 2.18 |
| 10-18 16:57 | +10 stop | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-18 16:57 | +20 | XRP | DOWN | 0.67 | 0.91 | 2.17 |
| 10-18 16:57 | +15 | XRP | DOWN | 0.67 | 0.91 | 2.17 |
| 10-18 16:57 | +10 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-18 16:57 | +5 | XRP | DOWN | 0.67 | 0.80 | 1.02 |
| 10-18 16:56 | +10 stop | ETH | DOWN | 0.68 | 0.44 | -2.74 |
| 10-18 16:56 | +10 stop | BNB | DOWN | 0.50 | 0.29 | -2.43 |
| 10-18 16:55 | +10 stop | SOL | UP | 0.67 | 0.89 | 1.97 |
| 10-18 16:55 | +10 stop | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-18 16:52 | +10 stop | BNB | UP | 0.58 | 0.41 | -2.05 |
| 10-18 16:51 | +10 stop | XRP | UP | 0.61 | 0.46 | -1.85 |
| 10-18 16:51 | +10 stop | ETH | UP | 0.59 | 0.33 | -2.93 |
| 10-18 16:51 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.70 |
| 10-18 16:51 | +10 stop | BNB | DOWN | 0.56 | 0.41 | -1.85 |
| 10-18 16:50 | +10 stop | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-18 16:50 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-18 16:49 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-18 16:48 | +10 stop | HYPE | UP | 0.64 | 0.39 | -2.80 |
| 10-18 16:48 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-18 16:48 | +10 stop | NEAR | DOWN | 0.50 | 0.35 | -1.84 |
| 10-18 16:47 | +10 stop | ZEC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-18 16:47 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 16:47 | +10 stop | DOGE | UP | 0.49 | 0.59 | 0.65 |
| 10-18 16:47 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 10-18 16:47 | +20 | XRP | DOWN | 0.63 | 0.86 | 2.04 |
| 10-18 16:47 | +15 | XRP | DOWN | 0.63 | 0.81 | 1.52 |
| 10-18 16:47 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-18 16:47 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.48 |
| 10-18 16:46 | +10 stop | BNB | DOWN | 0.68 | 0.49 | -2.24 |
| 10-18 16:46 | +20 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-18 16:46 | +15 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-18 16:46 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-18 16:46 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-18 16:46 | +10 stop | DOGE | DOWN | 0.65 | 0.45 | -2.34 |
| 10-18 16:46 | +20 | DOGE | DOWN | 0.65 | yes | -6.66 |
| 10-18 16:46 | +15 | DOGE | DOWN | 0.65 | yes | -6.66 |
| 10-18 16:46 | +10 | DOGE | DOWN | 0.65 | yes | -6.66 |
| 10-18 16:46 | +5 | DOGE | DOWN | 0.66 | yes | -6.76 |
| 10-18 16:46 | +10 stop | BTC | DOWN | 0.66 | 0.81 | 1.23 |
