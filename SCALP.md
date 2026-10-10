# Range-Scalp Bot

*Updated Sat Oct 10 10:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10265 | 8849 | 1416 (22) | 1 | $-3506.32 | -5.4% |
| **+10¢** | 7761 | 6113 | 1648 (34) | 1 | $-3351.34 | -6.9% |
| **+15¢** | 6553 | 4809 | 1744 (49) | 2 | $-2814.39 | -6.8% |
| **+20¢** | 5822 | 4007 | 1815 (63) | 2 | $-2381.87 | -6.5% |
| **+10¢ (15¢ stop)** | 12604 | 12567 | 37 (24) | 1 | $-4947.13 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 10:01 | +10 stop | BNB | UP | 0.41 | 0.53 | 0.85 |
| 10-10 10:01 | +20 | BNB | UP | 0.41 | open |  |
| 10-10 10:01 | +15 | BNB | UP | 0.41 | open |  |
| 10-10 10:01 | +10 | BNB | UP | 0.41 | 0.53 | 0.85 |
| 10-10 10:01 | +5 | BNB | UP | 0.41 | 0.53 | 0.85 |
| 10-10 10:01 | +10 stop | BTC | UP | 0.58 | open |  |
| 10-10 10:01 | +20 | BTC | UP | 0.58 | open |  |
| 10-10 10:01 | +15 | BTC | UP | 0.58 | open |  |
| 10-10 10:01 | +10 | BTC | UP | 0.58 | open |  |
| 10-10 10:01 | +5 | BTC | UP | 0.58 | open |  |
| 10-10 09:59 | +10 stop | ETH | UP | 0.64 | 0.82 | 1.52 |
| 10-10 09:55 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.82 |
| 10-10 09:55 | +10 stop | SOL | DOWN | 0.67 | 0.85 | 1.55 |
| 10-10 09:55 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.85 |
| 10-10 09:55 | +15 | SOL | DOWN | 0.67 | 0.85 | 1.54 |
| 10-10 09:55 | +10 | SOL | DOWN | 0.68 | 0.85 | 1.45 |
| 10-10 09:55 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-10 09:55 | +10 stop | BNB | UP | 0.60 | 0.37 | -2.64 |
| 10-10 09:55 | +10 | BNB | UP | 0.60 | no | -6.17 |
| 10-10 09:55 | +10 stop | ETH | UP | 0.61 | 0.71 | 0.68 |
| 10-10 09:53 | +10 stop | DOGE | UP | 0.56 | 0.76 | 1.69 |
| 10-10 09:53 | +10 stop | ETH | DOWN | 0.62 | 0.41 | -2.44 |
| 10-10 09:53 | +20 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-10 09:53 | +15 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-10 09:53 | +10 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-10 09:53 | +5 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-10 09:53 | +10 stop | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-10 09:53 | +10 | BNB | UP | 0.53 | 0.67 | 1.06 |
| 10-10 09:52 | +10 stop | DOGE | DOWN | 0.60 | 0.42 | -2.20 |
| 10-10 09:52 | +15 | DOGE | DOWN | 0.60 | 0.91 | 2.78 |
| 10-10 09:52 | +10 | DOGE | DOWN | 0.60 | 0.73 | 0.94 |
| 10-10 09:52 | +5 | DOGE | DOWN | 0.60 | 0.73 | 0.94 |
| 10-10 09:52 | +10 stop | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-10 09:52 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-10 09:52 | +10 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-10 09:52 | +5 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 10-10 09:51 | +10 stop | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-10 09:51 | +20 | DOGE | DOWN | 0.56 | 0.91 | 3.22 |
| 10-10 09:51 | +15 | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-10 09:51 | +10 | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
