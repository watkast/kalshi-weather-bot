# Range-Scalp Bot

*Updated Fri Nov 20 00:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65562 | 57229 | 8333 (124) | 0 | $-17557.60 | -4.3% |
| **+10¢** | 48969 | 39227 | 9742 (165) | 0 | $-16313.60 | -5.3% |
| **+15¢** | 41065 | 30557 | 10508 (211) | 2 | $-14677.53 | -5.7% |
| **+20¢** | 36562 | 25522 | 11040 (266) | 2 | $-12996.72 | -5.7% |
| **+10¢ (15¢ stop)** | 79810 | 79646 | 164 (98) | 0 | $-29349.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 00:53 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-20 00:53 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-20 00:53 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-20 00:53 | +10 | SOL | DOWN | 0.69 | 0.83 | 1.15 |
| 11-20 00:53 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-20 00:53 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 00:53 | +10 | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-20 00:53 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-20 00:52 | +10 stop | BTC | DOWN | 0.54 | 0.71 | 1.37 |
| 11-20 00:52 | +20 | BTC | DOWN | 0.54 | 0.74 | 1.68 |
| 11-20 00:52 | +15 | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-20 00:52 | +10 | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-20 00:52 | +5 | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-20 00:52 | +10 stop | ETH | DOWN | 0.52 | 0.64 | 0.85 |
| 11-20 00:52 | +20 | ETH | DOWN | 0.57 | 0.81 | 2.11 |
| 11-20 00:52 | +15 | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 11-20 00:52 | +10 | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 11-20 00:52 | +5 | ETH | DOWN | 0.56 | 0.64 | 0.45 |
| 11-20 00:47 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 00:47 | +20 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 11-20 00:47 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 11-20 00:47 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 00:47 | +5 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-20 00:47 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 00:47 | +10 | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 00:47 | +5 | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 00:47 | +10 stop | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-20 00:47 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 11-20 00:47 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-20 00:47 | +10 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-20 00:47 | +5 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-20 00:46 | +10 stop | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-20 00:46 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-20 00:46 | +15 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-20 00:46 | +10 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-20 00:46 | +5 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-20 00:46 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-20 00:46 | +20 | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 11-20 00:46 | +15 | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 11-20 00:46 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
