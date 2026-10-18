# Range-Scalp Bot

*Updated Sun Oct 18 22:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23052 | 20042 | 3010 (30) | 5 | $-6889.16 | -4.7% |
| **+10¢** | 17337 | 13863 | 3474 (44) | 5 | $-6179.75 | -5.7% |
| **+15¢** | 14536 | 10789 | 3747 (66) | 5 | $-5634.51 | -6.2% |
| **+20¢** | 12876 | 8958 | 3918 (84) | 5 | $-5005.06 | -6.2% |
| **+10¢ (15¢ stop)** | 28388 | 28337 | 51 (30) | 0 | $-10866.32 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 22:55 | +10 stop | ZEC | UP | 0.69 | 0.84 | 1.22 |
| 10-18 22:53 | +10 stop | BTC | UP | 0.61 | 0.72 | 0.78 |
| 10-18 22:52 | +10 stop | ETH | UP | 0.63 | 0.83 | 1.73 |
| 10-18 22:52 | +10 | BNB | UP | 0.67 | 0.80 | 1.02 |
| 10-18 22:52 | +5 | BNB | UP | 0.67 | 0.80 | 1.02 |
| 10-18 22:52 | +10 stop | ZEC | UP | 0.64 | 0.85 | 1.84 |
| 10-18 22:51 | +10 stop | BNB | UP | 0.68 | 0.80 | 0.88 |
| 10-18 22:51 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-18 22:49 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-18 22:49 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-18 22:49 | +10 stop | BNB | DOWN | 0.61 | 0.41 | -2.34 |
| 10-18 22:49 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-18 22:47 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 10-18 22:47 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-18 22:47 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.74 |
| 10-18 22:47 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 10-18 22:47 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-18 22:47 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-18 22:47 | +10 | ETH | DOWN | 0.62 | open |  |
| 10-18 22:47 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 10-18 22:47 | +10 stop | DOGE | DOWN | 0.60 | 0.45 | -1.87 |
| 10-18 22:47 | +20 | DOGE | DOWN | 0.60 | open |  |
| 10-18 22:47 | +15 | DOGE | DOWN | 0.60 | open |  |
| 10-18 22:47 | +10 | DOGE | DOWN | 0.60 | open |  |
| 10-18 22:47 | +5 | DOGE | DOWN | 0.60 | open |  |
| 10-18 22:47 | +10 stop | ZEC | DOWN | 0.65 | 0.46 | -2.24 |
| 10-18 22:47 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-18 22:47 | +15 | ZEC | DOWN | 0.65 | open |  |
| 10-18 22:47 | +10 | ZEC | DOWN | 0.65 | open |  |
| 10-18 22:47 | +5 | ZEC | DOWN | 0.65 | open |  |
| 10-18 22:46 | +10 stop | BTC | DOWN | 0.59 | 0.37 | -2.54 |
| 10-18 22:46 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-18 22:46 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-18 22:46 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-18 22:46 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-18 22:46 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-18 22:46 | +20 | HYPE | UP | 0.62 | 0.85 | 2.04 |
| 10-18 22:46 | +15 | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 10-18 22:46 | +10 | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-18 22:46 | +5 | HYPE | UP | 0.62 | 0.70 | 0.48 |
