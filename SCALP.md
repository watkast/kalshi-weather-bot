# Range-Scalp Bot

*Updated Wed Oct 07 20:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6768 | 5874 | 894 (10) | 5 | $-2070.63 | -4.8% |
| **+10¢** | 5139 | 4093 | 1046 (17) | 5 | $-1932.67 | -6.0% |
| **+15¢** | 4302 | 3201 | 1101 (21) | 6 | $-1610.71 | -6.0% |
| **+20¢** | 3845 | 2698 | 1147 (28) | 7 | $-1281.43 | -5.3% |
| **+10¢ (15¢ stop)** | 8216 | 8199 | 17 (10) | 3 | $-2930.77 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 20:24 | +10 stop | XRP | UP | 0.22 | open |  |
| 10-07 20:24 | +10 | XRP | UP | 0.22 | open |  |
| 10-07 20:24 | +5 | XRP | UP | 0.22 | open |  |
| 10-07 20:23 | +10 stop | ETH | UP | 0.59 | open |  |
| 10-07 20:21 | +10 stop | ETH | DOWN | 0.59 | 0.36 | -2.64 |
| 10-07 20:21 | +5 | BNB | UP | 0.50 | 0.56 | 0.24 |
| 10-07 20:21 | +10 stop | NEAR | UP | 0.66 | 0.42 | -2.74 |
| 10-07 20:21 | +10 | NEAR | UP | 0.66 | open |  |
| 10-07 20:21 | +5 | NEAR | UP | 0.66 | open |  |
| 10-07 20:20 | +10 stop | BNB | UP | 0.54 | open |  |
| 10-07 20:20 | +10 | BNB | UP | 0.54 | open |  |
| 10-07 20:20 | +5 | BNB | UP | 0.54 | 0.63 | 0.55 |
| 10-07 20:20 | +5 | BTC | UP | 0.58 | open |  |
| 10-07 20:20 | +10 stop | ETH | UP | 0.56 | 0.39 | -2.05 |
| 10-07 20:20 | +10 | ETH | UP | 0.56 | open |  |
| 10-07 20:20 | +5 | SOL | UP | 0.67 | open |  |
| 10-07 20:19 | +10 stop | BTC | UP | 0.60 | 0.38 | -2.54 |
| 10-07 20:19 | +10 stop | BNB | UP | 0.56 | 0.66 | 0.67 |
| 10-07 20:19 | +10 | BNB | UP | 0.56 | 0.66 | 0.67 |
| 10-07 20:19 | +5 | BNB | UP | 0.57 | 0.66 | 0.57 |
| 10-07 20:18 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 20:18 | +20 | DOGE | UP | 0.69 | open |  |
| 10-07 20:18 | +15 | DOGE | UP | 0.69 | 0.87 | 1.58 |
| 10-07 20:18 | +10 | DOGE | UP | 0.69 | 0.80 | 0.84 |
| 10-07 20:18 | +5 | DOGE | UP | 0.69 | 0.76 | 0.43 |
| 10-07 20:18 | +10 stop | SOL | UP | 0.59 | 0.71 | 0.88 |
| 10-07 20:18 | +10 | SOL | UP | 0.59 | 0.71 | 0.88 |
| 10-07 20:18 | +5 | SOL | UP | 0.59 | 0.65 | 0.27 |
| 10-07 20:18 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 10-07 20:17 | +10 stop | ETH | UP | 0.69 | 0.51 | -2.12 |
| 10-07 20:17 | +5 | ETH | UP | 0.69 | open |  |
| 10-07 20:17 | +5 | NEAR | UP | 0.62 | 0.71 | 0.58 |
| 10-07 20:16 | +5 | ETH | UP | 0.65 | 0.74 | 0.60 |
| 10-07 20:16 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.89 |
| 10-07 20:16 | +20 | SOL | UP | 0.64 | open |  |
| 10-07 20:16 | +15 | SOL | UP | 0.64 | open |  |
| 10-07 20:16 | +10 | SOL | UP | 0.64 | 0.75 | 0.79 |
| 10-07 20:16 | +5 | SOL | UP | 0.64 | 0.75 | 0.79 |
| 10-07 20:16 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-07 20:16 | +20 | BNB | UP | 0.69 | open |  |
