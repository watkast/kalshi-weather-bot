# Range-Scalp Bot

*Updated Wed Nov 04 08:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46992 | 40923 | 6069 (72) | 3 | $-13515.83 | -4.6% |
| **+10¢** | 35103 | 28067 | 7036 (96) | 3 | $-12324.19 | -5.6% |
| **+15¢** | 29395 | 21824 | 7571 (124) | 4 | $-11263.61 | -6.1% |
| **+20¢** | 26116 | 18185 | 7931 (164) | 4 | $-9927.41 | -6.1% |
| **+10¢ (15¢ stop)** | 57268 | 57175 | 93 (56) | 3 | $-21339.68 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 08:50 | +10 stop | ETH | UP | 0.64 | 0.75 | 0.79 |
| 11-04 08:50 | +15 | ETH | UP | 0.64 | open |  |
| 11-04 08:50 | +10 | ETH | UP | 0.64 | 0.75 | 0.79 |
| 11-04 08:50 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 11-04 08:50 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 11-04 08:50 | +10 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 11-04 08:50 | +5 | ZEC | UP | 0.58 | open |  |
| 11-04 08:50 | +5 | ZEC | UP | 0.60 | 0.68 | 0.47 |
| 11-04 08:50 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-04 08:49 | +5 | SOL | UP | 0.71 | 0.80 | 0.63 |
| 11-04 08:48 | +10 stop | DOGE | UP | 0.67 | open |  |
| 11-04 08:48 | +15 | DOGE | UP | 0.67 | open |  |
| 11-04 08:48 | +10 | DOGE | UP | 0.67 | open |  |
| 11-04 08:48 | +5 | DOGE | UP | 0.68 | open |  |
| 11-04 08:48 | +15 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 11-04 08:48 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-04 08:48 | +20 | ZEC | UP | 0.65 | open |  |
| 11-04 08:48 | +15 | ZEC | UP | 0.65 | open |  |
| 11-04 08:48 | +10 | ZEC | UP | 0.65 | open |  |
| 11-04 08:48 | +5 | ZEC | UP | 0.65 | 0.71 | 0.29 |
| 11-04 08:48 | +5 | XRP | UP | 0.65 | 0.81 | 1.33 |
| 11-04 08:48 | +5 | SOL | UP | 0.61 | 0.68 | 0.37 |
| 11-04 08:48 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 11-04 08:48 | +10 | BNB | UP | 0.68 | 0.81 | 1.03 |
| 11-04 08:48 | +5 | BNB | UP | 0.68 | 0.75 | 0.40 |
| 11-04 08:47 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 11-04 08:47 | +20 | NEAR | DOWN | 0.58 | open |  |
| 11-04 08:47 | +15 | NEAR | DOWN | 0.58 | open |  |
| 11-04 08:47 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-04 08:47 | +5 | NEAR | DOWN | 0.58 | 0.64 | 0.25 |
| 11-04 08:46 | +5 | ETH | UP | 0.59 | 0.69 | 0.68 |
| 11-04 08:46 | +10 stop | XRP | UP | 0.63 | 0.81 | 1.52 |
| 11-04 08:46 | +20 | XRP | UP | 0.63 | 0.85 | 1.94 |
| 11-04 08:46 | +15 | XRP | UP | 0.63 | 0.81 | 1.52 |
| 11-04 08:46 | +10 | XRP | UP | 0.63 | 0.81 | 1.52 |
| 11-04 08:46 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 11-04 08:46 | +10 stop | ZEC | UP | 0.52 | 0.69 | 1.37 |
| 11-04 08:46 | +20 | ZEC | UP | 0.52 | 0.72 | 1.67 |
| 11-04 08:46 | +15 | ZEC | UP | 0.52 | 0.69 | 1.37 |
| 11-04 08:46 | +10 | ZEC | UP | 0.52 | 0.69 | 1.37 |
