# Range-Scalp Bot

*Updated Tue Oct 27 07:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36206 | 31613 | 4593 (43) | 4 | $-10024.17 | -4.4% |
| **+10¢** | 27068 | 21755 | 5313 (65) | 4 | $-8857.75 | -5.2% |
| **+15¢** | 22649 | 16942 | 5707 (89) | 4 | $-7834.05 | -5.5% |
| **+20¢** | 20072 | 14093 | 5979 (112) | 4 | $-6866.21 | -5.4% |
| **+10¢ (15¢ stop)** | 44404 | 44341 | 63 (33) | 0 | $-16902.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 07:47 | +10 stop | NEAR | DOWN | 0.13 | 0.58 | 4.24 |
| 10-27 07:47 | +20 | NEAR | DOWN | 0.15 | 0.58 | 4.03 |
| 10-27 07:47 | +15 | NEAR | DOWN | 0.16 | 0.58 | 3.92 |
| 10-27 07:47 | +10 | NEAR | DOWN | 0.15 | 0.58 | 4.03 |
| 10-27 07:47 | +5 | NEAR | DOWN | 0.15 | 0.58 | 4.03 |
| 10-27 07:46 | +10 stop | ETH | UP | 0.53 | 0.69 | 1.27 |
| 10-27 07:46 | +20 | ETH | UP | 0.53 | 0.79 | 2.30 |
| 10-27 07:46 | +15 | ETH | UP | 0.53 | 0.69 | 1.27 |
| 10-27 07:46 | +10 | ETH | UP | 0.53 | 0.69 | 1.27 |
| 10-27 07:46 | +5 | ETH | UP | 0.53 | 0.69 | 1.27 |
| 10-27 07:46 | +10 stop | BTC | DOWN | 0.57 | 0.16 | -4.38 |
| 10-27 07:46 | +20 | BTC | DOWN | 0.57 | open |  |
| 10-27 07:46 | +15 | BTC | DOWN | 0.57 | open |  |
| 10-27 07:46 | +10 | BTC | DOWN | 0.57 | open |  |
| 10-27 07:46 | +5 | BTC | DOWN | 0.57 | open |  |
| 10-27 07:46 | +10 stop | HYPE | DOWN | 0.55 | 0.19 | -3.89 |
| 10-27 07:46 | +20 | HYPE | DOWN | 0.55 | open |  |
| 10-27 07:46 | +15 | HYPE | DOWN | 0.55 | open |  |
| 10-27 07:46 | +10 | HYPE | DOWN | 0.55 | open |  |
| 10-27 07:46 | +5 | HYPE | DOWN | 0.55 | open |  |
| 10-27 07:46 | +10 stop | XRP | DOWN | 0.60 | 0.21 | -4.18 |
| 10-27 07:46 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-27 07:46 | +15 | XRP | DOWN | 0.60 | open |  |
| 10-27 07:46 | +10 | XRP | DOWN | 0.60 | open |  |
| 10-27 07:46 | +5 | XRP | DOWN | 0.60 | open |  |
| 10-27 07:46 | +10 stop | SOL | DOWN | 0.54 | 0.20 | -3.70 |
| 10-27 07:46 | +20 | SOL | DOWN | 0.54 | open |  |
| 10-27 07:46 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-27 07:46 | +10 | SOL | DOWN | 0.54 | open |  |
| 10-27 07:46 | +5 | SOL | DOWN | 0.54 | open |  |
| 10-27 07:43 | +10 stop | ETH | DOWN | 0.67 | 0.80 | 1.02 |
| 10-27 07:43 | +15 | ETH | DOWN | 0.67 | 0.93 | 2.34 |
| 10-27 07:43 | +10 | ETH | DOWN | 0.68 | 0.80 | 0.92 |
| 10-27 07:43 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 07:41 | +10 stop | SOL | UP | 0.41 | 0.57 | 1.25 |
| 10-27 07:41 | +5 | SOL | UP | 0.41 | 0.57 | 1.25 |
| 10-27 07:40 | +10 stop | ETH | DOWN | 0.62 | 0.47 | -1.85 |
| 10-27 07:40 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-27 07:40 | +20 | DOGE | UP | 0.64 | 0.90 | 2.36 |
| 10-27 07:40 | +15 | DOGE | UP | 0.64 | 0.82 | 1.52 |
