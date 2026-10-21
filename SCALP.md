# Range-Scalp Bot

*Updated Wed Oct 21 06:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26811 | 23345 | 3466 (33) | 0 | $-7860.94 | -4.7% |
| **+10¢** | 20181 | 16176 | 4005 (48) | 1 | $-6962.74 | -5.5% |
| **+15¢** | 16897 | 12592 | 4305 (72) | 1 | $-6176.12 | -5.8% |
| **+20¢** | 14960 | 10446 | 4514 (91) | 1 | $-5557.37 | -5.9% |
| **+10¢ (15¢ stop)** | 32881 | 32828 | 53 (30) | 0 | $-12136.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 06:28 | +10 stop | XRP | DOWN | 0.65 | 0.34 | -3.42 |
| 10-21 06:27 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-21 06:26 | +10 stop | XRP | UP | 0.56 | 0.41 | -1.85 |
| 10-21 06:26 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 10-21 06:25 | +10 stop | DOGE | UP | 0.60 | 0.45 | -1.85 |
| 10-21 06:25 | +10 stop | ETH | UP | 0.68 | 0.53 | -1.84 |
| 10-21 06:23 | +10 stop | ETH | DOWN | 0.48 | 0.32 | -1.94 |
| 10-21 06:23 | +5 | XRP | UP | 0.56 | 0.67 | 0.76 |
| 10-21 06:23 | +5 | DOGE | DOWN | 0.58 | 0.66 | 0.46 |
| 10-21 06:22 | +10 stop | DOGE | DOWN | 0.56 | 0.41 | -1.85 |
| 10-21 06:22 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-21 06:22 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-21 06:22 | +10 stop | BTC | UP | 0.63 | 0.76 | 1.00 |
| 10-21 06:22 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-21 06:22 | +10 stop | BNB | DOWN | 0.51 | 0.19 | -3.49 |
| 10-21 06:22 | +10 stop | BNB | DOWN | 0.56 | 0.67 | 0.76 |
| 10-21 06:22 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 10-21 06:22 | +10 stop | XRP | DOWN | 0.56 | 0.32 | -2.74 |
| 10-21 06:22 | +20 | XRP | DOWN | 0.56 | open |  |
| 10-21 06:22 | +15 | XRP | DOWN | 0.56 | open |  |
| 10-21 06:22 | +10 | XRP | DOWN | 0.56 | open |  |
| 10-21 06:22 | +5 | XRP | DOWN | 0.56 | 0.65 | 0.56 |
| 10-21 06:21 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.86 |
| 10-21 06:21 | +5 | BTC | UP | 0.55 | 0.62 | 0.35 |
| 10-21 06:20 | +10 stop | SOL | UP | 0.71 | 0.54 | -2.03 |
| 10-21 06:20 | +20 | SOL | UP | 0.70 | 0.90 | 1.80 |
| 10-21 06:20 | +15 | SOL | UP | 0.70 | 0.85 | 1.26 |
| 10-21 06:20 | +10 | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-21 06:20 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-21 06:20 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 10-21 06:19 | +10 stop | ETH | UP | 0.61 | 0.45 | -1.95 |
| 10-21 06:18 | +10 stop | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 10-21 06:18 | +10 stop | BTC | UP | 0.66 | 0.50 | -1.94 |
| 10-21 06:18 | +20 | BTC | UP | 0.66 | 0.89 | 2.07 |
| 10-21 06:18 | +15 | BTC | UP | 0.66 | 0.84 | 1.54 |
| 10-21 06:18 | +10 | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-21 06:18 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 10-21 06:18 | +10 stop | HYPE | UP | 0.64 | 0.83 | 1.63 |
| 10-21 06:18 | +20 | HYPE | UP | 0.64 | 0.84 | 1.73 |
| 10-21 06:18 | +15 | HYPE | UP | 0.64 | 0.83 | 1.63 |
