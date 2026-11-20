# Range-Scalp Bot

*Updated Fri Nov 20 23:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66710 | 58219 | 8491 (128) | 3 | $-17943.20 | -4.3% |
| **+10¢** | 49816 | 39893 | 9923 (170) | 5 | $-16678.01 | -5.3% |
| **+15¢** | 41776 | 31078 | 10698 (217) | 6 | $-14977.37 | -5.7% |
| **+20¢** | 37192 | 25956 | 11236 (273) | 5 | $-13261.57 | -5.7% |
| **+10¢ (15¢ stop)** | 81240 | 81074 | 166 (100) | 1 | $-29996.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 23:52 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.43 |
| 11-20 23:52 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.04 |
| 11-20 23:52 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-20 23:52 | +10 | XRP | DOWN | 0.66 | 0.79 | 1.04 |
| 11-20 23:52 | +5 | XRP | DOWN | 0.66 | 0.74 | 0.51 |
| 11-20 23:51 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 11-20 23:51 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-20 23:51 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-20 23:50 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 11-20 23:49 | +10 stop | ZEC | UP | 0.51 | 0.31 | -2.33 |
| 11-20 23:49 | +10 stop | DOGE | UP | 0.60 | 0.34 | -2.93 |
| 11-20 23:49 | +5 | ETH | DOWN | 0.54 | 0.59 | 0.15 |
| 11-20 23:49 | +10 stop | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 11-20 23:48 | +10 stop | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 11-20 23:48 | +5 | ETH | DOWN | 0.52 | 0.60 | 0.45 |
| 11-20 23:48 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-20 23:48 | +10 stop | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 23:48 | +20 | BTC | DOWN | 0.70 | 0.92 | 2.04 |
| 11-20 23:48 | +15 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-20 23:48 | +10 | BTC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 23:48 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-20 23:48 | +10 stop | XRP | UP | 0.52 | 0.29 | -2.63 |
| 11-20 23:47 | +5 | BNB | UP | 0.48 | 0.57 | 0.54 |
| 11-20 23:47 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 11-20 23:47 | +15 | ETH | UP | 0.55 | open |  |
| 11-20 23:47 | +10 | ETH | UP | 0.56 | open |  |
| 11-20 23:47 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 11-20 23:47 | +10 stop | SOL | UP | 0.58 | 0.33 | -2.84 |
| 11-20 23:47 | +20 | SOL | UP | 0.58 | open |  |
| 11-20 23:47 | +15 | SOL | UP | 0.58 | open |  |
| 11-20 23:47 | +10 | SOL | UP | 0.58 | open |  |
| 11-20 23:47 | +5 | SOL | UP | 0.58 | open |  |
| 11-20 23:47 | +5 | DOGE | UP | 0.66 | open |  |
| 11-20 23:47 | +10 stop | BNB | UP | 0.55 | 0.36 | -2.25 |
| 11-20 23:47 | +20 | BNB | UP | 0.55 | open |  |
| 11-20 23:47 | +15 | BNB | UP | 0.55 | open |  |
| 11-20 23:47 | +10 | BNB | UP | 0.55 | open |  |
| 11-20 23:47 | +5 | BNB | UP | 0.55 | 0.63 | 0.45 |
| 11-20 23:47 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 11-20 23:47 | +20 | ZEC | UP | 0.67 | open |  |
