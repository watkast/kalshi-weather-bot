# Range-Scalp Bot

*Updated Fri Nov 20 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65707 | 57354 | 8353 (124) | 4 | $-17614.24 | -4.3% |
| **+10¢** | 49076 | 39309 | 9767 (165) | 6 | $-16382.27 | -5.3% |
| **+15¢** | 41158 | 30621 | 10537 (211) | 6 | $-14761.47 | -5.7% |
| **+20¢** | 36638 | 25570 | 11068 (267) | 6 | $-13068.75 | -5.7% |
| **+10¢ (15¢ stop)** | 79980 | 79816 | 164 (98) | 2 | $-29426.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 02:25 | +10 stop | SOL | DOWN | 0.49 | open |  |
| 11-20 02:25 | +15 | SOL | DOWN | 0.49 | open |  |
| 11-20 02:25 | +10 | SOL | DOWN | 0.49 | open |  |
| 11-20 02:25 | +5 | SOL | DOWN | 0.50 | open |  |
| 11-20 02:25 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-20 02:25 | +20 | ETH | UP | 0.40 | 0.64 | 2.06 |
| 11-20 02:25 | +10 stop | BNB | UP | 0.37 | 0.56 | 1.53 |
| 11-20 02:24 | +10 stop | ETH | UP | 0.63 | 0.37 | -2.94 |
| 11-20 02:24 | +15 | ETH | UP | 0.63 | open |  |
| 11-20 02:24 | +10 stop | XRP | UP | 0.60 | 0.74 | 1.09 |
| 11-20 02:24 | +10 stop | BNB | DOWN | 0.60 | 0.38 | -2.54 |
| 11-20 02:23 | +10 stop | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-20 02:23 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 11-20 02:23 | +20 | XRP | UP | 0.61 | open |  |
| 11-20 02:23 | +15 | XRP | UP | 0.62 | open |  |
| 11-20 02:23 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 11-20 02:23 | +10 | ETH | UP | 0.62 | open |  |
| 11-20 02:23 | +5 | ETH | UP | 0.63 | open |  |
| 11-20 02:23 | +10 stop | XRP | UP | 0.69 | 0.54 | -1.83 |
| 11-20 02:23 | +10 | XRP | UP | 0.69 | open |  |
| 11-20 02:23 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 11-20 02:22 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 11-20 02:22 | +20 | BTC | UP | 0.70 | open |  |
| 11-20 02:22 | +15 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 11-20 02:22 | +10 | BTC | UP | 0.70 | 0.80 | 0.73 |
| 11-20 02:22 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 11-20 02:22 | +10 stop | BNB | DOWN | 0.68 | 0.52 | -1.94 |
| 11-20 02:22 | +10 stop | ETH | UP | 0.45 | 0.55 | 0.64 |
| 11-20 02:22 | +20 | ETH | UP | 0.44 | 0.67 | 1.96 |
| 11-20 02:22 | +15 | ETH | UP | 0.43 | 0.60 | 1.35 |
| 11-20 02:22 | +10 | ETH | UP | 0.43 | 0.55 | 0.84 |
| 11-20 02:22 | +5 | ETH | UP | 0.43 | 0.55 | 0.84 |
| 11-20 02:22 | +10 stop | XRP | UP | 0.44 | 0.55 | 0.74 |
| 11-20 02:22 | +20 | XRP | UP | 0.44 | 0.66 | 1.86 |
| 11-20 02:22 | +15 | XRP | UP | 0.46 | 0.66 | 1.66 |
| 11-20 02:22 | +10 | XRP | UP | 0.46 | 0.57 | 0.74 |
| 11-20 02:22 | +5 | XRP | UP | 0.46 | 0.55 | 0.54 |
| 11-20 02:21 | +10 stop | SOL | UP | 0.61 | 0.81 | 1.72 |
| 11-20 02:21 | +20 | SOL | UP | 0.63 | open |  |
| 11-20 02:21 | +15 | SOL | UP | 0.63 | 0.81 | 1.52 |
