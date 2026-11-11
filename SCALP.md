# Range-Scalp Bot

*Updated Wed Nov 11 01:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55220 | 48166 | 7054 (94) | 2 | $-15024.41 | -4.3% |
| **+10¢** | 41254 | 33024 | 8230 (124) | 4 | $-13954.10 | -5.4% |
| **+15¢** | 34586 | 25716 | 8870 (158) | 6 | $-12685.47 | -5.8% |
| **+20¢** | 30791 | 21485 | 9306 (207) | 7 | $-11092.73 | -5.7% |
| **+10¢ (15¢ stop)** | 67250 | 67132 | 118 (73) | 4 | $-24783.43 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 01:47 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-11 01:47 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 11-11 01:47 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-11 01:47 | +5 | ETH | DOWN | 0.66 | open |  |
| 11-11 01:46 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-11 01:46 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-11 01:46 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-11 01:46 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 01:46 | +5 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 01:46 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-11 01:46 | +20 | BTC | DOWN | 0.64 | open |  |
| 11-11 01:46 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-11 01:46 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-11 01:46 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-11 01:46 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 11-11 01:46 | +20 | NEAR | DOWN | 0.58 | open |  |
| 11-11 01:46 | +15 | NEAR | DOWN | 0.58 | open |  |
| 11-11 01:46 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-11 01:46 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 11-11 01:46 | +10 stop | HYPE | DOWN | 0.66 | 0.50 | -1.94 |
| 11-11 01:46 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-11 01:46 | +15 | HYPE | DOWN | 0.65 | open |  |
| 11-11 01:46 | +10 | HYPE | DOWN | 0.65 | open |  |
| 11-11 01:46 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.25 |
| 11-11 01:46 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 11-11 01:46 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-11 01:46 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-11 01:46 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-11 01:46 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.40 |
| 11-11 01:46 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 11-11 01:46 | +20 | ETH | DOWN | 0.57 | open |  |
| 11-11 01:46 | +15 | ETH | DOWN | 0.57 | open |  |
| 11-11 01:46 | +10 | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 11-11 01:46 | +5 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 11-11 01:46 | +10 stop | ZEC | DOWN | 0.66 | 0.80 | 1.12 |
| 11-11 01:46 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-11 01:46 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-11 01:46 | +10 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-11 01:46 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-11 01:36 | +10 stop | ETH | UP | 0.71 | 0.86 | 1.26 |
