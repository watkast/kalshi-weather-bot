# Range-Scalp Bot

*Updated Fri Nov 20 22:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66610 | 58134 | 8476 (128) | 3 | $-17906.59 | -4.3% |
| **+10¢** | 49744 | 39836 | 9908 (170) | 4 | $-16645.55 | -5.3% |
| **+15¢** | 41718 | 31036 | 10682 (217) | 4 | $-14943.48 | -5.7% |
| **+20¢** | 37140 | 25922 | 11218 (273) | 4 | $-13215.88 | -5.7% |
| **+10¢ (15¢ stop)** | 81115 | 80949 | 166 (100) | 4 | $-29962.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 22:30 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 11-20 22:30 | +20 | ETH | DOWN | 0.69 | open |  |
| 11-20 22:30 | +15 | ETH | DOWN | 0.69 | open |  |
| 11-20 22:30 | +10 | ETH | DOWN | 0.69 | open |  |
| 11-20 22:30 | +5 | ETH | DOWN | 0.69 | open |  |
| 11-20 22:30 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-20 22:30 | +20 | BTC | DOWN | 0.68 | open |  |
| 11-20 22:30 | +15 | BTC | DOWN | 0.68 | open |  |
| 11-20 22:30 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-20 22:30 | +5 | BTC | DOWN | 0.68 | open |  |
| 11-20 22:30 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-20 22:30 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-20 22:30 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-20 22:30 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-20 22:30 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-20 22:30 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-20 22:30 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-20 22:30 | +15 | BNB | DOWN | 0.66 | open |  |
| 11-20 22:30 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-20 22:30 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-20 22:27 | +10 stop | DOGE | UP | 0.52 | 0.72 | 1.67 |
| 11-20 22:27 | +10 | DOGE | UP | 0.52 | 0.72 | 1.67 |
| 11-20 22:27 | +5 | DOGE | UP | 0.52 | 0.61 | 0.55 |
| 11-20 22:26 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 11-20 22:25 | +10 stop | DOGE | UP | 0.65 | 0.42 | -2.64 |
| 11-20 22:25 | +20 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 11-20 22:25 | +15 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 11-20 22:25 | +10 | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 11-20 22:25 | +5 | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 11-20 22:24 | +15 | ETH | DOWN | 0.55 | 0.77 | 1.89 |
| 11-20 22:24 | +10 stop | NEAR | DOWN | 0.48 | 0.60 | 0.85 |
| 11-20 22:24 | +5 | NEAR | DOWN | 0.49 | 0.60 | 0.75 |
| 11-20 22:23 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 11-20 22:23 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-20 22:23 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-20 22:23 | +5 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-20 22:23 | +10 stop | BTC | DOWN | 0.51 | 0.69 | 1.47 |
| 11-20 22:23 | +10 | BTC | DOWN | 0.51 | 0.69 | 1.47 |
| 11-20 22:23 | +10 stop | HYPE | UP | 0.56 | 0.75 | 1.58 |
| 11-20 22:22 | +5 | BTC | UP | 0.70 | no | -7.15 |
