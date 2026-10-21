# Range-Scalp Bot

*Updated Wed Oct 21 00:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26431 | 23018 | 3413 (33) | 3 | $-7725.23 | -4.6% |
| **+10¢** | 19889 | 15949 | 3940 (48) | 3 | $-6809.11 | -5.4% |
| **+15¢** | 16644 | 12405 | 4239 (72) | 4 | $-6071.31 | -5.8% |
| **+20¢** | 14728 | 10282 | 4446 (91) | 5 | $-5472.56 | -5.9% |
| **+10¢ (15¢ stop)** | 32376 | 32323 | 53 (30) | 3 | $-11819.71 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 00:16 | +10 stop | DOGE | UP | 0.68 | open |  |
| 10-21 00:16 | +20 | DOGE | UP | 0.68 | open |  |
| 10-21 00:16 | +15 | DOGE | UP | 0.68 | open |  |
| 10-21 00:16 | +10 | DOGE | UP | 0.68 | open |  |
| 10-21 00:16 | +5 | DOGE | UP | 0.68 | open |  |
| 10-21 00:16 | +10 stop | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-21 00:16 | +20 | HYPE | UP | 0.60 | open |  |
| 10-21 00:16 | +15 | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-21 00:16 | +10 | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-21 00:16 | +5 | HYPE | UP | 0.60 | 0.77 | 1.40 |
| 10-21 00:16 | +15 | ETH | UP | 0.67 | open |  |
| 10-21 00:16 | +10 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 10-21 00:16 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 10-21 00:15 | +10 stop | BNB | UP | 0.56 | open |  |
| 10-21 00:15 | +20 | BNB | UP | 0.56 | open |  |
| 10-21 00:15 | +15 | BNB | UP | 0.59 | open |  |
| 10-21 00:15 | +10 | BNB | UP | 0.59 | open |  |
| 10-21 00:15 | +5 | BNB | UP | 0.62 | open |  |
| 10-21 00:15 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.73 |
| 10-21 00:15 | +20 | ETH | UP | 0.71 | open |  |
| 10-21 00:15 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-21 00:15 | +20 | BTC | UP | 0.71 | open |  |
| 10-21 00:15 | +15 | BTC | UP | 0.71 | open |  |
| 10-21 00:15 | +10 | BTC | UP | 0.71 | open |  |
| 10-21 00:15 | +5 | BTC | UP | 0.71 | open |  |
| 10-21 00:12 | +10 stop | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-21 00:12 | +10 | ETH | DOWN | 0.57 | 0.81 | 2.11 |
| 10-21 00:12 | +5 | ETH | DOWN | 0.57 | 0.66 | 0.56 |
| 10-21 00:11 | +10 stop | SOL | DOWN | 0.40 | 0.55 | 1.15 |
| 10-21 00:10 | +10 stop | SOL | DOWN | 0.62 | 0.46 | -1.95 |
| 10-21 00:10 | +10 | SOL | DOWN | 0.62 | yes | -6.37 |
| 10-21 00:10 | +5 | SOL | DOWN | 0.62 | yes | -6.37 |
| 10-21 00:10 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-21 00:10 | +10 stop | SOL | DOWN | 0.53 | 0.63 | 0.65 |
| 10-21 00:10 | +10 | SOL | DOWN | 0.53 | 0.63 | 0.65 |
| 10-21 00:10 | +5 | SOL | DOWN | 0.54 | 0.63 | 0.58 |
| 10-21 00:10 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-21 00:10 | +20 | ETH | DOWN | 0.70 | yes | -7.15 |
| 10-21 00:10 | +15 | ETH | DOWN | 0.70 | yes | -7.15 |
| 10-21 00:10 | +10 | ETH | DOWN | 0.70 | 0.81 | 0.84 |
