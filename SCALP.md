# Range-Scalp Bot

*Updated Sat Oct 31 05:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41834 | 36502 | 5332 (54) | 4 | $-11746.30 | -4.5% |
| **+10¢** | 31183 | 25010 | 6173 (78) | 5 | $-10509.29 | -5.4% |
| **+15¢** | 26066 | 19411 | 6655 (106) | 5 | $-9597.77 | -5.9% |
| **+20¢** | 23146 | 16178 | 6968 (137) | 5 | $-8442.88 | -5.8% |
| **+10¢ (15¢ stop)** | 50995 | 50920 | 75 (41) | 2 | $-19238.31 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 05:41 | +10 stop | XRP | UP | 0.64 | open |  |
| 10-31 05:41 | +10 | XRP | UP | 0.64 | open |  |
| 10-31 05:41 | +5 | XRP | UP | 0.64 | open |  |
| 10-31 05:40 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 10-31 05:40 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-31 05:40 | +5 | BTC | DOWN | 0.66 | open |  |
| 10-31 05:39 | +10 stop | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-31 05:39 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-31 05:39 | +15 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-31 05:39 | +10 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-31 05:39 | +5 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-31 05:39 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-31 05:39 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-31 05:39 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-31 05:39 | +10 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 10-31 05:39 | +5 | BTC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-31 05:39 | +5 | DOGE | DOWN | 0.58 | 0.67 | 0.56 |
| 10-31 05:37 | +10 stop | ETH | DOWN | 0.67 | 0.50 | -2.04 |
| 10-31 05:37 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-31 05:37 | +15 | ETH | DOWN | 0.67 | open |  |
| 10-31 05:37 | +10 | ETH | DOWN | 0.67 | open |  |
| 10-31 05:37 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 10-31 05:37 | +10 stop | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 10-31 05:37 | +10 stop | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 05:37 | +20 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-31 05:37 | +15 | DOGE | DOWN | 0.62 | 0.84 | 1.93 |
| 10-31 05:37 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 05:37 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-31 05:36 | +10 stop | BNB | DOWN | 0.65 | 0.47 | -2.12 |
| 10-31 05:36 | +5 | BNB | DOWN | 0.65 | 0.86 | 1.87 |
| 10-31 05:35 | +10 stop | ZEC | DOWN | 0.66 | 0.45 | -2.44 |
| 10-31 05:35 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-31 05:35 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-31 05:35 | +10 | ZEC | DOWN | 0.66 | open |  |
| 10-31 05:35 | +5 | ZEC | DOWN | 0.66 | open |  |
| 10-31 05:35 | +10 stop | NEAR | DOWN | 0.67 | 0.39 | -3.13 |
| 10-31 05:35 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-31 05:35 | +15 | NEAR | DOWN | 0.67 | open |  |
| 10-31 05:35 | +10 | NEAR | DOWN | 0.67 | open |  |
| 10-31 05:35 | +5 | NEAR | DOWN | 0.67 | open |  |
