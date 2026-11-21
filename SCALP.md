# Range-Scalp Bot

*Updated Sat Nov 21 00:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66760 | 58260 | 8500 (128) | 3 | $-17979.12 | -4.3% |
| **+10¢** | 49851 | 39918 | 9933 (170) | 6 | $-16709.23 | -5.3% |
| **+15¢** | 41809 | 31100 | 10709 (217) | 6 | $-15009.25 | -5.7% |
| **+20¢** | 37215 | 25967 | 11248 (273) | 8 | $-13311.37 | -5.7% |
| **+10¢ (15¢ stop)** | 81294 | 81128 | 166 (100) | 5 | $-30006.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 00:34 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 11-21 00:34 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-21 00:34 | +10 | BNB | DOWN | 0.67 | open |  |
| 11-21 00:34 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-21 00:33 | +10 stop | ETH | UP | 0.70 | open |  |
| 11-21 00:33 | +10 | ETH | UP | 0.70 | open |  |
| 11-21 00:33 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 11-21 00:33 | +10 stop | XRP | DOWN | 0.59 | open |  |
| 11-21 00:33 | +10 | XRP | DOWN | 0.59 | open |  |
| 11-21 00:33 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 11-21 00:33 | +10 stop | BNB | DOWN | 0.45 | 0.63 | 1.45 |
| 11-21 00:33 | +15 | BNB | DOWN | 0.45 | 0.63 | 1.45 |
| 11-21 00:33 | +10 | BNB | DOWN | 0.45 | 0.63 | 1.45 |
| 11-21 00:33 | +5 | BNB | DOWN | 0.45 | 0.63 | 1.45 |
| 11-21 00:33 | +10 stop | XRP | UP | 0.39 | 0.53 | 1.05 |
| 11-21 00:33 | +20 | XRP | UP | 0.39 | open |  |
| 11-21 00:33 | +15 | XRP | UP | 0.39 | open |  |
| 11-21 00:33 | +10 | XRP | UP | 0.39 | 0.53 | 1.05 |
| 11-21 00:33 | +5 | XRP | UP | 0.39 | 0.53 | 1.05 |
| 11-21 00:32 | +5 | BTC | UP | 0.69 | open |  |
| 11-21 00:31 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-21 00:31 | +20 | ETH | UP | 0.62 | open |  |
| 11-21 00:31 | +15 | ETH | UP | 0.62 | open |  |
| 11-21 00:31 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-21 00:31 | +5 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-21 00:30 | +10 stop | BTC | UP | 0.59 | open |  |
| 11-21 00:30 | +20 | BTC | UP | 0.59 | open |  |
| 11-21 00:30 | +15 | BTC | UP | 0.59 | open |  |
| 11-21 00:30 | +10 | BTC | UP | 0.59 | open |  |
| 11-21 00:30 | +5 | BTC | UP | 0.59 | 0.65 | 0.27 |
| 11-21 00:30 | +10 stop | SOL | UP | 0.68 | open |  |
| 11-21 00:30 | +20 | SOL | UP | 0.68 | open |  |
| 11-21 00:30 | +15 | SOL | UP | 0.68 | open |  |
| 11-21 00:30 | +10 | SOL | UP | 0.68 | open |  |
| 11-21 00:30 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 11-21 00:30 | +10 stop | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 11-21 00:30 | +20 | DOGE | UP | 0.69 | open |  |
| 11-21 00:30 | +15 | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 11-21 00:30 | +10 | DOGE | UP | 0.69 | 0.82 | 1.04 |
| 11-21 00:30 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
