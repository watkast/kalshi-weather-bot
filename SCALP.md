# Range-Scalp Bot

*Updated Sun Nov 22 21:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69132 | 60322 | 8810 (145) | 2 | $-18609.69 | -4.3% |
| **+10¢** | 51591 | 41304 | 10287 (188) | 2 | $-17257.49 | -5.3% |
| **+15¢** | 43238 | 32151 | 11087 (240) | 2 | $-15468.42 | -5.7% |
| **+20¢** | 38505 | 26853 | 11652 (299) | 2 | $-13759.69 | -5.7% |
| **+10¢ (15¢ stop)** | 84192 | 84003 | 189 (117) | 2 | $-31022.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 21:40 | +10 stop | SOL | UP | 0.61 | open |  |
| 11-22 21:40 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 11-22 21:38 | +10 stop | SOL | DOWN | 0.56 | 0.39 | -2.05 |
| 11-22 21:38 | +5 | SOL | DOWN | 0.56 | open |  |
| 11-22 21:38 | +10 stop | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 11-22 21:38 | +5 | SOL | DOWN | 0.55 | 0.65 | 0.66 |
| 11-22 21:37 | +10 stop | BTC | DOWN | 0.66 | 0.51 | -1.84 |
| 11-22 21:37 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-22 21:37 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-22 21:37 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-22 21:34 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 11-22 21:34 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-22 21:34 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-22 21:34 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.25 |
| 11-22 21:34 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-22 21:34 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-22 21:34 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-22 21:34 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-22 21:34 | +5 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-22 21:31 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-22 21:31 | +20 | ETH | DOWN | 0.67 | 0.87 | 1.76 |
| 11-22 21:31 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-22 21:31 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 11-22 21:31 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 11-22 21:31 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.70 |
| 11-22 21:31 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-22 21:31 | +15 | SOL | DOWN | 0.61 | 0.78 | 1.41 |
| 11-22 21:31 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.69 |
| 11-22 21:31 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 11-22 21:31 | +10 stop | DOGE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-22 21:31 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-22 21:31 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-22 21:31 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 21:31 | +5 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 21:31 | +10 stop | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 21:31 | +20 | HYPE | DOWN | 0.61 | 0.82 | 1.82 |
| 11-22 21:31 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 11-22 21:31 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 21:31 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-22 21:28 | +10 stop | ZEC | UP | 0.46 | 0.62 | 1.27 |
