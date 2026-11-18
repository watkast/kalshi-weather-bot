# Range-Scalp Bot

*Updated Wed Nov 18 18:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64335 | 56110 | 8225 (124) | 2 | $-17579.86 | -4.3% |
| **+10¢** | 48051 | 38431 | 9620 (165) | 2 | $-16420.67 | -5.4% |
| **+15¢** | 40285 | 29918 | 10367 (210) | 2 | $-14845.52 | -5.9% |
| **+20¢** | 35873 | 24992 | 10881 (265) | 2 | $-13132.17 | -5.8% |
| **+10¢ (15¢ stop)** | 78271 | 78107 | 164 (98) | 1 | $-28849.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 18:25 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 11-18 18:22 | +5 | BTC | UP | 0.66 | 0.75 | 0.60 |
| 11-18 18:21 | +10 | ETH | UP | 0.64 | 0.78 | 1.10 |
| 11-18 18:21 | +5 | ETH | UP | 0.64 | 0.78 | 1.10 |
| 11-18 18:21 | +5 | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-18 18:21 | +10 stop | NEAR | DOWN | 0.71 | 0.43 | -3.13 |
| 11-18 18:21 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-18 18:21 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-18 18:21 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-18 18:21 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-18 18:21 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 18:21 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-18 18:20 | +10 stop | ETH | UP | 0.66 | 0.78 | 0.91 |
| 11-18 18:20 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.99 |
| 11-18 18:19 | +10 stop | BNB | DOWN | 0.54 | 0.37 | -2.05 |
| 11-18 18:19 | +10 stop | SOL | DOWN | 0.54 | 0.39 | -1.85 |
| 11-18 18:19 | +10 stop | ETH | DOWN | 0.64 | 0.43 | -2.45 |
| 11-18 18:19 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-18 18:18 | +10 stop | XRP | DOWN | 0.69 | 0.51 | -2.13 |
| 11-18 18:18 | +10 stop | ZEC | DOWN | 0.59 | 0.34 | -2.83 |
| 11-18 18:18 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-18 18:18 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-18 18:18 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-18 18:18 | +5 | ZEC | DOWN | 0.61 | open |  |
| 11-18 18:18 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 11-18 18:18 | +5 | HYPE | UP | 0.61 | 0.66 | 0.18 |
| 11-18 18:17 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 11-18 18:16 | +10 stop | XRP | UP | 0.70 | 0.54 | -1.93 |
| 11-18 18:16 | +20 | XRP | UP | 0.70 | 0.91 | 1.86 |
| 11-18 18:16 | +15 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 11-18 18:16 | +10 | XRP | UP | 0.70 | 0.82 | 0.94 |
| 11-18 18:16 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 11-18 18:16 | +10 stop | SOL | UP | 0.61 | 0.45 | -1.95 |
| 11-18 18:16 | +20 | SOL | UP | 0.62 | 0.84 | 1.93 |
| 11-18 18:16 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-18 18:16 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 11-18 18:16 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-18 18:16 | +10 stop | DOGE | UP | 0.56 | 0.41 | -1.85 |
| 11-18 18:16 | +20 | DOGE | UP | 0.56 | 0.76 | 1.69 |
| 11-18 18:16 | +15 | DOGE | UP | 0.56 | 0.76 | 1.69 |
