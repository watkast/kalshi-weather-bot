# Range-Scalp Bot

*Updated Mon Oct 05 13:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3865 | 3328 | 537 (3) | 7 | $-1337.68 | -5.5% |
| **+10¢** | 2993 | 2375 | 618 (4) | 9 | $-1209.59 | -6.4% |
| **+15¢** | 2515 | 1865 | 650 (7) | 9 | $-1034.17 | -6.5% |
| **+20¢** | 2245 | 1567 | 678 (12) | 9 | $-865.29 | -6.1% |
| **+10¢ (15¢ stop)** | 4793 | 4792 | 1 (1) | 0 | $-1798.93 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 13:47 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-05 13:47 | +10 stop | XRP | UP | 0.71 | 0.83 | 0.95 |
| 10-05 13:47 | +10 stop | ETH | UP | 0.70 | 0.87 | 1.47 |
| 10-05 13:47 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-05 13:47 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-05 13:47 | +10 stop | NEAR | UP | 0.71 | 0.81 | 0.78 |
| 10-05 13:46 | +10 stop | ZEC | DOWN | 0.64 | 0.40 | -2.74 |
| 10-05 13:46 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-05 13:46 | +15 | ZEC | DOWN | 0.66 | open |  |
| 10-05 13:46 | +10 | ZEC | DOWN | 0.63 | open |  |
| 10-05 13:46 | +5 | ZEC | DOWN | 0.63 | open |  |
| 10-05 13:46 | +5 | ETH | DOWN | 0.44 | 0.67 | 1.96 |
| 10-05 13:46 | +10 stop | HYPE | DOWN | 0.58 | 0.41 | -2.05 |
| 10-05 13:46 | +20 | HYPE | DOWN | 0.58 | open |  |
| 10-05 13:46 | +15 | HYPE | DOWN | 0.58 | open |  |
| 10-05 13:46 | +10 | HYPE | DOWN | 0.58 | open |  |
| 10-05 13:46 | +5 | HYPE | DOWN | 0.58 | open |  |
| 10-05 13:46 | +10 stop | NEAR | DOWN | 0.54 | 0.35 | -2.24 |
| 10-05 13:46 | +20 | NEAR | DOWN | 0.54 | open |  |
| 10-05 13:46 | +15 | NEAR | DOWN | 0.54 | open |  |
| 10-05 13:46 | +10 | NEAR | DOWN | 0.54 | open |  |
| 10-05 13:46 | +5 | NEAR | DOWN | 0.54 | open |  |
| 10-05 13:46 | +10 stop | DOGE | DOWN | 0.67 | 0.48 | -2.28 |
| 10-05 13:46 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-05 13:46 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-05 13:46 | +10 | DOGE | DOWN | 0.67 | open |  |
| 10-05 13:46 | +5 | DOGE | DOWN | 0.67 | open |  |
| 10-05 13:46 | +10 stop | SOL | DOWN | 0.69 | 0.52 | -2.03 |
| 10-05 13:46 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-05 13:46 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-05 13:46 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-05 13:46 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-05 13:46 | +10 stop | XRP | DOWN | 0.70 | 0.52 | -2.12 |
| 10-05 13:46 | +20 | XRP | DOWN | 0.70 | open |  |
| 10-05 13:46 | +15 | XRP | DOWN | 0.70 | open |  |
| 10-05 13:46 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-05 13:46 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-05 13:46 | +10 stop | BTC | DOWN | 0.63 | 0.46 | -2.05 |
| 10-05 13:46 | +20 | BTC | DOWN | 0.63 | open |  |
| 10-05 13:46 | +15 | BTC | DOWN | 0.62 | open |  |
