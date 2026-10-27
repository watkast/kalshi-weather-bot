# Range-Scalp Bot

*Updated Tue Oct 27 02:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35819 | 31262 | 4557 (43) | 5 | $-10011.09 | -4.4% |
| **+10¢** | 26777 | 21507 | 5270 (65) | 6 | $-8841.36 | -5.2% |
| **+15¢** | 22408 | 16744 | 5664 (89) | 8 | $-7876.08 | -5.6% |
| **+20¢** | 19861 | 13927 | 5934 (112) | 9 | $-6928.03 | -5.6% |
| **+10¢ (15¢ stop)** | 43902 | 43839 | 63 (33) | 5 | $-16685.01 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 02:04 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 02:04 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 10-27 02:04 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 10-27 02:04 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-27 02:03 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-27 02:03 | +20 | XRP | DOWN | 0.65 | open |  |
| 10-27 02:03 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-27 02:03 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-27 02:03 | +5 | XRP | DOWN | 0.66 | open |  |
| 10-27 02:03 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.39 |
| 10-27 02:03 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 10-27 02:02 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 10-27 02:02 | +10 stop | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-27 02:02 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-27 02:02 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-27 02:02 | +10 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-27 02:02 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
| 10-27 02:02 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 02:02 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-27 02:02 | +10 stop | NEAR | DOWN | 0.67 | open |  |
| 10-27 02:02 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-27 02:02 | +15 | NEAR | DOWN | 0.66 | open |  |
| 10-27 02:02 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-27 02:02 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.50 |
| 10-27 02:02 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 02:02 | +20 | ZEC | DOWN | 0.71 | open |  |
| 10-27 02:02 | +15 | ZEC | DOWN | 0.71 | open |  |
| 10-27 02:02 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 02:02 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 10-27 02:02 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 02:02 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-27 02:02 | +15 | DOGE | DOWN | 0.69 | open |  |
| 10-27 02:02 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 02:02 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-27 02:02 | +10 stop | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 10-27 02:02 | +10 stop | SOL | DOWN | 0.46 | 0.61 | 1.15 |
| 10-27 02:00 | +10 stop | ETH | UP | 0.56 | 0.38 | -2.15 |
| 10-27 02:00 | +20 | ETH | UP | 0.56 | open |  |
| 10-27 02:00 | +15 | ETH | UP | 0.56 | open |  |
| 10-27 02:00 | +10 | ETH | UP | 0.56 | open |  |
