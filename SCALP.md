# Range-Scalp Bot

*Updated Tue Oct 27 23:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37236 | 32507 | 4729 (45) | 2 | $-10350.47 | -4.4% |
| **+10¢** | 27807 | 22327 | 5480 (67) | 3 | $-9259.51 | -5.3% |
| **+15¢** | 23266 | 17381 | 5885 (91) | 6 | $-8219.99 | -5.6% |
| **+20¢** | 20614 | 14456 | 6158 (116) | 9 | $-7197.92 | -5.6% |
| **+10¢ (15¢ stop)** | 45611 | 45546 | 65 (34) | 3 | $-17383.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 23:33 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 10-27 23:33 | +20 | DOGE | DOWN | 0.63 | open |  |
| 10-27 23:33 | +15 | DOGE | DOWN | 0.63 | open |  |
| 10-27 23:33 | +10 | DOGE | DOWN | 0.63 | open |  |
| 10-27 23:33 | +5 | DOGE | DOWN | 0.63 | open |  |
| 10-27 23:32 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-27 23:31 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 23:31 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-27 23:31 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-27 23:31 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 23:31 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 10-27 23:31 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-27 23:31 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-27 23:31 | +15 | ZEC | DOWN | 0.65 | open |  |
| 10-27 23:31 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-27 23:31 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-27 23:31 | +10 stop | HYPE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-27 23:31 | +20 | HYPE | DOWN | 0.63 | open |  |
| 10-27 23:31 | +15 | HYPE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-27 23:31 | +10 | HYPE | DOWN | 0.63 | 0.82 | 1.62 |
| 10-27 23:31 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-27 23:31 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 10-27 23:31 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-27 23:31 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-27 23:31 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-27 23:31 | +5 | XRP | DOWN | 0.60 | open |  |
| 10-27 23:31 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-27 23:31 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-27 23:31 | +15 | SOL | DOWN | 0.66 | open |  |
| 10-27 23:31 | +10 | SOL | DOWN | 0.66 | open |  |
| 10-27 23:31 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 10-27 23:31 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 23:31 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-27 23:31 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-27 23:31 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 23:31 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 23:31 | +10 stop | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-27 23:31 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-27 23:31 | +15 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-27 23:31 | +10 | BTC | DOWN | 0.64 | 0.80 | 1.31 |
