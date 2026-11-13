# Range-Scalp Bot

*Updated Fri Nov 13 05:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57897 | 50506 | 7391 (101) | 1 | $-15713.75 | -4.3% |
| **+10¢** | 43260 | 34625 | 8635 (133) | 3 | $-14666.42 | -5.4% |
| **+15¢** | 36266 | 26972 | 9294 (167) | 4 | $-13210.37 | -5.8% |
| **+20¢** | 32304 | 22548 | 9756 (217) | 5 | $-11607.18 | -5.7% |
| **+10¢ (15¢ stop)** | 70563 | 70435 | 128 (78) | 3 | $-25976.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 05:16 | +10 stop | BTC | UP | 0.63 | open |  |
| 11-13 05:16 | +20 | BTC | UP | 0.63 | open |  |
| 11-13 05:16 | +15 | BTC | UP | 0.63 | open |  |
| 11-13 05:16 | +10 | BTC | UP | 0.63 | open |  |
| 11-13 05:16 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 11-13 05:16 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-13 05:16 | +20 | BNB | UP | 0.68 | open |  |
| 11-13 05:16 | +15 | BNB | UP | 0.68 | open |  |
| 11-13 05:16 | +10 | BNB | UP | 0.68 | open |  |
| 11-13 05:16 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 11-13 05:16 | +10 stop | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-13 05:16 | +20 | SOL | UP | 0.60 | open |  |
| 11-13 05:16 | +15 | SOL | UP | 0.60 | open |  |
| 11-13 05:16 | +10 | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-13 05:16 | +5 | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-13 05:16 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-13 05:16 | +20 | ETH | UP | 0.59 | open |  |
| 11-13 05:16 | +15 | ETH | UP | 0.59 | open |  |
| 11-13 05:16 | +10 | ETH | UP | 0.59 | open |  |
| 11-13 05:16 | +5 | ETH | UP | 0.59 | open |  |
| 11-13 05:16 | +10 stop | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-13 05:16 | +20 | DOGE | UP | 0.63 | open |  |
| 11-13 05:16 | +15 | DOGE | UP | 0.63 | 0.78 | 1.20 |
| 11-13 05:16 | +10 | DOGE | UP | 0.63 | 0.74 | 0.79 |
| 11-13 05:16 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
| 11-13 05:12 | +10 stop | ZEC | UP | 0.68 | 0.89 | 1.87 |
| 11-13 05:12 | +10 stop | ETH | DOWN | 0.48 | 0.65 | 1.36 |
| 11-13 05:12 | +5 | ETH | DOWN | 0.48 | 0.65 | 1.36 |
| 11-13 05:11 | +10 stop | SOL | UP | 0.46 | 0.60 | 1.05 |
| 11-13 05:11 | +10 stop | ETH | DOWN | 0.61 | 0.44 | -2.05 |
| 11-13 05:11 | +20 | ETH | DOWN | 0.59 | yes | -6.10 |
| 11-13 05:11 | +15 | ETH | DOWN | 0.59 | yes | -6.10 |
| 11-13 05:11 | +10 | ETH | DOWN | 0.59 | yes | -6.10 |
| 11-13 05:11 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.44 |
| 11-13 05:11 | +10 stop | XRP | DOWN | 0.59 | 0.37 | -2.54 |
| 11-13 05:11 | +20 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-13 05:11 | +15 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-13 05:11 | +10 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-13 05:11 | +5 | XRP | DOWN | 0.59 | yes | -6.07 |
| 11-13 05:10 | +10 stop | ZEC | UP | 0.69 | 0.82 | 1.03 |
