# Range-Scalp Bot

*Updated Tue Oct 06 17:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5222 | 4525 | 697 (7) | 4 | $-1619.08 | -4.9% |
| **+10¢** | 3991 | 3176 | 815 (12) | 4 | $-1503.68 | -6.0% |
| **+15¢** | 3347 | 2484 | 863 (15) | 5 | $-1303.94 | -6.2% |
| **+20¢** | 2995 | 2098 | 897 (22) | 5 | $-1035.64 | -5.5% |
| **+10¢ (15¢ stop)** | 6377 | 6362 | 15 (9) | 0 | $-2333.40 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 17:07 | +10 stop | ETH | UP | 0.69 | 0.54 | -1.83 |
| 10-06 17:07 | +5 | ETH | UP | 0.69 | open |  |
| 10-06 17:06 | +10 | HYPE | UP | 0.66 | 0.79 | 1.04 |
| 10-06 17:06 | +5 | HYPE | UP | 0.66 | 0.79 | 1.04 |
| 10-06 17:05 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 10-06 17:05 | +10 | SOL | UP | 0.63 | 0.81 | 1.52 |
| 10-06 17:05 | +10 stop | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-06 17:05 | +5 | SOL | UP | 0.65 | 0.81 | 1.33 |
| 10-06 17:05 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 10-06 17:05 | +10 stop | BTC | DOWN | 0.65 | 0.43 | -2.54 |
| 10-06 17:04 | +5 | HYPE | UP | 0.64 | 0.69 | 0.18 |
| 10-06 17:04 | +10 stop | XRP | DOWN | 0.58 | 0.36 | -2.55 |
| 10-06 17:04 | +10 | XRP | DOWN | 0.58 | open |  |
| 10-06 17:04 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-06 17:04 | +10 stop | DOGE | DOWN | 0.59 | 0.70 | 0.78 |
| 10-06 17:04 | +10 | DOGE | DOWN | 0.59 | 0.70 | 0.79 |
| 10-06 17:04 | +5 | DOGE | DOWN | 0.59 | 0.70 | 0.79 |
| 10-06 17:04 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 10-06 17:04 | +5 | SOL | UP | 0.55 | 0.64 | 0.55 |
| 10-06 17:04 | +5 | ETH | DOWN | 0.56 | 0.62 | 0.25 |
| 10-06 17:04 | +10 stop | BNB | DOWN | 0.70 | 0.92 | 1.99 |
| 10-06 17:04 | +10 | BNB | DOWN | 0.70 | 0.92 | 1.99 |
| 10-06 17:04 | +5 | BNB | DOWN | 0.70 | 0.92 | 1.99 |
| 10-06 17:04 | +10 stop | DOGE | UP | 0.43 | 0.54 | 0.75 |
| 10-06 17:04 | +10 | DOGE | UP | 0.42 | 0.54 | 0.84 |
| 10-06 17:04 | +5 | DOGE | UP | 0.42 | 0.54 | 0.84 |
| 10-06 17:03 | +10 stop | SOL | UP | 0.65 | 0.47 | -2.14 |
| 10-06 17:03 | +10 stop | SOL | DOWN | 0.45 | 0.61 | 1.25 |
| 10-06 17:02 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.48 |
| 10-06 17:02 | +10 stop | ETH | DOWN | 0.63 | 0.46 | -2.05 |
| 10-06 17:02 | +20 | ETH | DOWN | 0.63 | open |  |
| 10-06 17:02 | +15 | ETH | DOWN | 0.63 | open |  |
| 10-06 17:02 | +10 | ETH | DOWN | 0.63 | open |  |
| 10-06 17:02 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-06 17:02 | +10 stop | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-06 17:02 | +20 | BNB | DOWN | 0.68 | 0.92 | 2.22 |
| 10-06 17:02 | +15 | BNB | DOWN | 0.68 | 0.92 | 2.22 |
| 10-06 17:02 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-06 17:02 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 10-06 17:02 | +10 stop | SOL | UP | 0.57 | 0.36 | -2.45 |
