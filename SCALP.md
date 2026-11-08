# Range-Scalp Bot

*Updated Sun Nov 08 02:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51882 | 45242 | 6640 (80) | 5 | $-14363.19 | -4.4% |
| **+10¢** | 38719 | 30973 | 7746 (106) | 6 | $-13387.42 | -5.5% |
| **+15¢** | 32423 | 24075 | 8348 (135) | 6 | $-12278.69 | -6.0% |
| **+20¢** | 28846 | 20095 | 8751 (180) | 6 | $-10802.10 | -6.0% |
| **+10¢ (15¢ stop)** | 63191 | 63088 | 103 (61) | 0 | $-23410.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 02:54 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.90 |
| 11-08 02:53 | +10 stop | BNB | UP | 0.64 | 0.47 | -2.05 |
| 11-08 02:52 | +5 | HYPE | DOWN | 0.48 | 0.65 | 1.36 |
| 11-08 02:52 | +10 stop | XRP | DOWN | 0.59 | 0.37 | -2.54 |
| 11-08 02:52 | +15 | XRP | DOWN | 0.59 | open |  |
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
| 11-08 02:47 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-08 02:47 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-08 02:47 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-08 02:47 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-08 02:47 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.85 |
| 11-08 02:47 | +10 | XRP | DOWN | 0.59 | open |  |
| 11-08 02:47 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-08 02:47 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-08 02:47 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-08 02:47 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-08 02:47 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-08 02:47 | +10 stop | BTC | DOWN | 0.61 | 0.43 | -2.15 |
| 11-08 02:47 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-08 02:47 | +15 | BTC | DOWN | 0.61 | open |  |
| 11-08 02:47 | +10 | BTC | DOWN | 0.61 | open |  |
| 11-08 02:47 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-08 02:47 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-08 02:46 | +10 stop | NEAR | DOWN | 0.66 | 0.51 | -1.85 |
| 11-08 02:46 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-08 02:46 | +15 | NEAR | DOWN | 0.66 | open |  |
| 11-08 02:46 | +10 | NEAR | DOWN | 0.66 | open |  |
