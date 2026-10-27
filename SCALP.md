# Range-Scalp Bot

*Updated Tue Oct 27 18:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36867 | 32190 | 4677 (44) | 0 | $-10232.09 | -4.4% |
| **+10¢** | 27542 | 22126 | 5416 (66) | 0 | $-9091.86 | -5.2% |
| **+15¢** | 23045 | 17233 | 5812 (90) | 0 | $-8015.24 | -5.5% |
| **+20¢** | 20424 | 14341 | 6083 (115) | 1 | $-6983.01 | -5.4% |
| **+10¢ (15¢ stop)** | 45168 | 45104 | 64 (33) | 0 | $-17213.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 17:57 | +10 stop | HYPE | DOWN | 0.43 | 0.61 | 1.45 |
| 10-27 17:57 | +20 | HYPE | DOWN | 0.43 | open |  |
| 10-27 17:57 | +15 | HYPE | DOWN | 0.43 | 0.61 | 1.45 |
| 10-27 17:57 | +10 | HYPE | DOWN | 0.43 | 0.61 | 1.45 |
| 10-27 17:57 | +5 | HYPE | DOWN | 0.44 | 0.61 | 1.35 |
| 10-27 17:50 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-27 17:50 | +20 | NEAR | DOWN | 0.60 | 0.83 | 2.03 |
| 10-27 17:50 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-27 17:50 | +10 | NEAR | DOWN | 0.60 | 0.71 | 0.78 |
| 10-27 17:50 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 10-27 17:50 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 17:50 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-27 17:50 | +15 | ETH | DOWN | 0.69 | 0.86 | 1.46 |
| 10-27 17:50 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-27 17:50 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 17:50 | +5 | BNB | DOWN | 0.71 | 0.79 | 0.53 |
| 10-27 17:49 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-27 17:48 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-27 17:48 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-27 17:48 | +10 stop | ETH | DOWN | 0.53 | 0.65 | 0.86 |
| 10-27 17:48 | +20 | ETH | DOWN | 0.53 | 0.75 | 1.88 |
| 10-27 17:48 | +15 | ETH | DOWN | 0.53 | 0.75 | 1.88 |
| 10-27 17:48 | +10 | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 10-27 17:48 | +5 | ETH | DOWN | 0.54 | 0.61 | 0.35 |
| 10-27 17:47 | +5 | BTC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-27 17:47 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-27 17:47 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-27 17:47 | +20 | BNB | DOWN | 0.66 | 0.90 | 2.20 |
| 10-27 17:47 | +15 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-27 17:47 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-27 17:47 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 10-27 17:47 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-27 17:47 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 10-27 17:46 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-27 17:46 | +20 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 10-27 17:46 | +15 | BTC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-27 17:46 | +10 | BTC | DOWN | 0.54 | 0.65 | 0.76 |
| 10-27 17:46 | +5 | BTC | DOWN | 0.54 | 0.60 | 0.25 |
| 10-27 17:46 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.79 |
| 10-27 17:46 | +20 | HYPE | DOWN | 0.69 | 0.91 | 1.93 |
