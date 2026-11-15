# Range-Scalp Bot

*Updated Sun Nov 15 13:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60796 | 53038 | 7758 (112) | 1 | $-16471.72 | -4.3% |
| **+10¢** | 45422 | 36326 | 9096 (150) | 1 | $-15545.07 | -5.4% |
| **+15¢** | 38044 | 28233 | 9811 (188) | 1 | $-14222.51 | -6.0% |
| **+20¢** | 33902 | 23611 | 10291 (240) | 1 | $-12517.83 | -5.9% |
| **+10¢ (15¢ stop)** | 73988 | 73837 | 151 (89) | 1 | $-27188.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 13:01 | +10 stop | ETH | DOWN | 0.44 | open |  |
| 11-15 13:01 | +20 | ETH | DOWN | 0.44 | open |  |
| 11-15 13:01 | +15 | ETH | DOWN | 0.45 | open |  |
| 11-15 13:01 | +10 | ETH | DOWN | 0.45 | open |  |
| 11-15 13:01 | +5 | ETH | DOWN | 0.45 | open |  |
| 11-15 12:58 | +10 stop | NEAR | DOWN | 0.52 | 0.18 | -3.69 |
| 11-15 12:58 | +10 | NEAR | DOWN | 0.54 | yes | -5.58 |
| 11-15 12:58 | +5 | NEAR | DOWN | 0.55 | yes | -5.63 |
| 11-15 12:57 | +10 stop | NEAR | DOWN | 0.07 | 0.59 | 4.97 |
| 11-15 12:57 | +10 | NEAR | DOWN | 0.07 | 0.59 | 4.96 |
| 11-15 12:57 | +5 | NEAR | DOWN | 0.08 | 0.59 | 4.85 |
| 11-15 12:56 | +10 stop | SOL | UP | 0.61 | 0.77 | 1.30 |
| 11-15 12:56 | +10 | SOL | UP | 0.61 | 0.77 | 1.30 |
| 11-15 12:56 | +5 | SOL | UP | 0.61 | 0.67 | 0.27 |
| 11-15 12:56 | +10 stop | BTC | DOWN | 0.53 | 0.67 | 1.06 |
| 11-15 12:56 | +5 | BTC | DOWN | 0.55 | 0.67 | 0.86 |
| 11-15 12:55 | +15 | BNB | UP | 0.63 | 0.95 | 2.99 |
| 11-15 12:55 | +10 | BNB | UP | 0.63 | 0.75 | 0.89 |
| 11-15 12:55 | +5 | BNB | UP | 0.63 | 0.75 | 0.89 |
| 11-15 12:54 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-15 12:54 | +10 stop | NEAR | UP | 0.63 | 0.44 | -2.25 |
| 11-15 12:54 | +10 stop | BTC | UP | 0.65 | 0.45 | -2.34 |
| 11-15 12:53 | +10 stop | XRP | UP | 0.42 | 0.55 | 0.94 |
| 11-15 12:53 | +10 stop | BNB | UP | 0.67 | 0.37 | -3.33 |
| 11-15 12:52 | +5 | NEAR | DOWN | 0.65 | 0.72 | 0.39 |
| 11-15 12:52 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-15 12:52 | +10 stop | HYPE | DOWN | 0.71 | 0.93 | 2.03 |
| 11-15 12:52 | +10 stop | BNB | UP | 0.48 | 0.62 | 1.05 |
| 11-15 12:52 | +10 stop | NEAR | DOWN | 0.63 | 0.36 | -3.04 |
| 11-15 12:52 | +15 | NEAR | DOWN | 0.63 | yes | -6.47 |
| 11-15 12:52 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-15 12:52 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-15 12:52 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-15 12:51 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-15 12:51 | +10 | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-15 12:51 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-15 12:50 | +10 stop | DOGE | UP | 0.56 | 0.70 | 1.02 |
| 11-15 12:49 | +10 stop | BNB | DOWN | 0.63 | 0.45 | -2.15 |
| 11-15 12:49 | +10 stop | XRP | DOWN | 0.69 | 0.47 | -2.53 |
| 11-15 12:49 | +10 stop | BTC | DOWN | 0.67 | 0.52 | -1.84 |
