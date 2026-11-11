# Range-Scalp Bot

*Updated Wed Nov 11 01:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55230 | 48176 | 7054 (94) | 1 | $-15018.33 | -4.3% |
| **+10¢** | 41262 | 33032 | 8230 (124) | 0 | $-13944.91 | -5.4% |
| **+15¢** | 34594 | 25724 | 8870 (158) | 0 | $-12673.72 | -5.8% |
| **+20¢** | 30798 | 21492 | 9306 (207) | 0 | $-11079.79 | -5.7% |
| **+10¢ (15¢ stop)** | 67264 | 67146 | 118 (73) | 0 | $-24785.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 01:51 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.01 |
| 11-11 01:51 | +10 stop | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 11-11 01:51 | +5 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 11-11 01:50 | +5 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 11-11 01:50 | +10 stop | HYPE | UP | 0.46 | 0.26 | -2.32 |
| 11-11 01:50 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-11 01:50 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-11 01:50 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-11 01:49 | +10 stop | ETH | DOWN | 0.53 | 0.69 | 1.27 |
| 11-11 01:49 | +15 | ETH | DOWN | 0.52 | 0.69 | 1.37 |
| 11-11 01:49 | +5 | ETH | DOWN | 0.52 | 0.57 | 0.14 |
| 11-11 01:49 | +10 stop | HYPE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-11 01:49 | +10 stop | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 11-11 01:49 | +5 | XRP | DOWN | 0.48 | 0.57 | 0.54 |
| 11-11 01:48 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 01:48 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 01:48 | +5 | SOL | DOWN | 0.65 | 0.74 | 0.60 |
| 11-11 01:48 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-11 01:48 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-11 01:48 | +10 | ZEC | DOWN | 0.67 | 0.81 | 1.15 |
| 11-11 01:48 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-11 01:48 | +10 stop | HYPE | UP | 0.61 | 0.37 | -2.74 |
| 11-11 01:48 | +5 | HYPE | UP | 0.61 | open |  |
| 11-11 01:48 | +10 | BTC | DOWN | 0.54 | 0.77 | 1.99 |
| 11-11 01:48 | +5 | BTC | DOWN | 0.54 | 0.63 | 0.55 |
| 11-11 01:47 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 11-11 01:47 | +10 stop | ETH | DOWN | 0.65 | 0.49 | -1.94 |
| 11-11 01:47 | +10 | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-11 01:47 | +5 | ETH | DOWN | 0.66 | 0.74 | 0.50 |
| 11-11 01:46 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-11 01:46 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 11-11 01:46 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 11-11 01:46 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 01:46 | +5 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 01:46 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-11 01:46 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-11 01:46 | +15 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 11-11 01:46 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 11-11 01:46 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-11 01:46 | +10 stop | NEAR | DOWN | 0.58 | 0.72 | 1.07 |
