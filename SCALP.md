# Range-Scalp Bot

*Updated Tue Oct 27 17:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36863 | 32186 | 4677 (44) | 1 | $-10234.45 | -4.4% |
| **+10¢** | 27537 | 22121 | 5416 (66) | 2 | $-9096.54 | -5.2% |
| **+15¢** | 23040 | 17228 | 5812 (90) | 2 | $-8022.20 | -5.5% |
| **+20¢** | 20417 | 14334 | 6083 (115) | 5 | $-6996.67 | -5.5% |
| **+10¢ (15¢ stop)** | 45162 | 45098 | 64 (33) | 3 | $-17219.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 17:50 | +5 | BNB | DOWN | 0.71 | open |  |
| 10-27 17:49 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 17:48 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 10-27 17:48 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 17:48 | +10 stop | ETH | DOWN | 0.53 | 0.65 | 0.86 |
| 10-27 17:48 | +20 | ETH | DOWN | 0.53 | 0.75 | 1.88 |
| 10-27 17:48 | +15 | ETH | DOWN | 0.53 | 0.75 | 1.88 |
| 10-27 17:48 | +10 | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 10-27 17:48 | +5 | ETH | DOWN | 0.54 | 0.61 | 0.35 |
| 10-27 17:47 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-27 17:47 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-27 17:47 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 10-27 17:47 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-27 17:47 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-27 17:47 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-27 17:47 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-27 17:47 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 10-27 17:47 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-27 17:46 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-27 17:46 | +20 | BTC | DOWN | 0.57 | open |  |
| 10-27 17:46 | +15 | BTC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-27 17:46 | +10 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-27 17:46 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-27 17:46 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.79 |
| 10-27 17:46 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-27 17:46 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-27 17:46 | +10 | HYPE | DOWN | 0.69 | 0.80 | 0.79 |
| 10-27 17:46 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.27 |
| 10-27 17:46 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 10-27 17:46 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 10-27 17:46 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 17:46 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-27 17:46 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-27 17:46 | +10 | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 17:46 | +5 | ZEC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-27 17:45 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.05 |
| 10-27 17:45 | +20 | XRP | DOWN | 0.57 | 0.78 | 1.77 |
| 10-27 17:45 | +15 | XRP | DOWN | 0.57 | 0.75 | 1.46 |
| 10-27 17:45 | +10 | XRP | DOWN | 0.57 | 0.71 | 1.05 |
| 10-27 17:45 | +5 | XRP | DOWN | 0.57 | 0.71 | 1.05 |
