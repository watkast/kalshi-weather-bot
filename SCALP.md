# Range-Scalp Bot

*Updated Sun Nov 01 00:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42930 | 37431 | 5499 (62) | 3 | $-12122.68 | -4.5% |
| **+10¢** | 32013 | 25654 | 6359 (84) | 3 | $-10876.78 | -5.4% |
| **+15¢** | 26781 | 19925 | 6856 (112) | 5 | $-9961.30 | -5.9% |
| **+20¢** | 23788 | 16602 | 7186 (145) | 4 | $-8822.05 | -5.9% |
| **+10¢ (15¢ stop)** | 52371 | 52288 | 83 (48) | 0 | $-19857.80 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 00:11 | +10 stop | ETH | UP | 0.45 | 0.66 | 1.76 |
| 11-01 00:11 | +10 | ETH | UP | 0.46 | 0.66 | 1.66 |
| 11-01 00:11 | +5 | ETH | UP | 0.46 | 0.66 | 1.66 |
| 11-01 00:10 | +10 stop | HYPE | DOWN | 0.68 | 0.52 | -1.98 |
| 11-01 00:10 | +10 stop | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-01 00:10 | +10 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-01 00:10 | +5 | ETH | UP | 0.56 | 0.66 | 0.66 |
| 11-01 00:10 | +5 | HYPE | DOWN | 0.70 | 0.80 | 0.68 |
| 11-01 00:10 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.10 |
| 11-01 00:10 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 00:09 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 11-01 00:09 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-01 00:08 | +10 stop | HYPE | UP | 0.67 | 0.48 | -2.24 |
| 11-01 00:08 | +20 | HYPE | UP | 0.67 | open |  |
| 11-01 00:08 | +15 | HYPE | UP | 0.67 | open |  |
| 11-01 00:08 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-01 00:08 | +5 | HYPE | UP | 0.66 | 0.72 | 0.26 |
| 11-01 00:08 | +10 stop | BNB | UP | 0.63 | 0.46 | -2.05 |
| 11-01 00:08 | +15 | BNB | UP | 0.63 | open |  |
| 11-01 00:08 | +10 | BNB | UP | 0.63 | open |  |
| 11-01 00:08 | +5 | BNB | UP | 0.63 | open |  |
| 11-01 00:07 | +10 stop | SOL | UP | 0.64 | 0.42 | -2.55 |
| 11-01 00:07 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 11-01 00:07 | +10 stop | DOGE | UP | 0.62 | 0.42 | -2.35 |
| 11-01 00:07 | +20 | DOGE | UP | 0.62 | open |  |
| 11-01 00:07 | +15 | DOGE | UP | 0.62 | open |  |
| 11-01 00:07 | +10 | DOGE | UP | 0.62 | open |  |
| 11-01 00:07 | +5 | DOGE | UP | 0.62 | open |  |
| 11-01 00:07 | +10 stop | SOL | UP | 0.56 | 0.66 | 0.66 |
| 11-01 00:07 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 11-01 00:07 | +15 | ETH | UP | 0.63 | open |  |
| 11-01 00:07 | +10 | ETH | UP | 0.62 | 0.76 | 1.10 |
| 11-01 00:07 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 11-01 00:07 | +10 stop | NEAR | UP | 0.58 | 0.40 | -2.15 |
| 11-01 00:06 | +10 stop | ZEC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-01 00:06 | +5 | ZEC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-01 00:05 | +10 stop | HYPE | DOWN | 0.58 | 0.40 | -2.15 |
| 11-01 00:04 | +10 stop | BNB | UP | 0.45 | 0.59 | 1.05 |
| 11-01 00:04 | +10 stop | XRP | DOWN | 0.64 | 0.46 | -2.15 |
| 11-01 00:04 | +20 | XRP | DOWN | 0.65 | open |  |
