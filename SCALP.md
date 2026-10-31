# Range-Scalp Bot

*Updated Sat Oct 31 06:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41905 | 36563 | 5342 (54) | 4 | $-11778.63 | -4.5% |
| **+10¢** | 31231 | 25046 | 6185 (78) | 5 | $-10549.68 | -5.4% |
| **+15¢** | 26105 | 19436 | 6669 (106) | 6 | $-9648.48 | -5.9% |
| **+20¢** | 23181 | 16198 | 6983 (137) | 6 | $-8494.83 | -5.8% |
| **+10¢ (15¢ stop)** | 51085 | 51010 | 75 (41) | 0 | $-19284.35 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 06:42 | +10 stop | SOL | UP | 0.68 | 0.79 | 0.82 |
| 10-31 06:42 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 10-31 06:41 | +5 | ETH | UP | 0.56 | 0.67 | 0.76 |
| 10-31 06:41 | +15 | DOGE | DOWN | 0.71 | open |  |
| 10-31 06:41 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-31 06:41 | +5 | DOGE | DOWN | 0.71 | 0.80 | 0.63 |
| 10-31 06:40 | +10 stop | ETH | UP | 0.60 | 0.77 | 1.40 |
| 10-31 06:40 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-31 06:39 | +10 stop | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-31 06:38 | +5 | ETH | DOWN | 0.50 | 0.55 | 0.14 |
| 10-31 06:38 | +10 stop | XRP | DOWN | 0.64 | 0.39 | -2.84 |
| 10-31 06:38 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-31 06:38 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-31 06:38 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-31 06:35 | +10 stop | SOL | DOWN | 0.66 | 0.36 | -3.33 |
| 10-31 06:35 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-31 06:35 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-31 06:35 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-31 06:35 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-31 06:35 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-31 06:35 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 10-31 06:35 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-31 06:34 | +10 stop | BTC | UP | 0.67 | 0.47 | -2.34 |
| 10-31 06:33 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-31 06:33 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-31 06:33 | +10 | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-31 06:33 | +5 | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-31 06:33 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-31 06:33 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 10-31 06:33 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 06:33 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-31 06:33 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-31 06:33 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 06:33 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 10-31 06:33 | +10 stop | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 10-31 06:33 | +10 | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 10-31 06:33 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 10-31 06:31 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.72 |
| 10-31 06:31 | +20 | ZEC | DOWN | 0.67 | 0.87 | 1.77 |
| 10-31 06:31 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.24 |
