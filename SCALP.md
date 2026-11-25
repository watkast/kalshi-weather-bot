# Range-Scalp Bot

*Updated Wed Nov 25 19:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72016 | 62860 | 9156 (158) | 5 | $-19161.04 | -4.2% |
| **+10¢** | 53726 | 43034 | 10692 (203) | 5 | $-17750.91 | -5.3% |
| **+15¢** | 44986 | 33469 | 11517 (260) | 6 | $-15842.10 | -5.6% |
| **+20¢** | 40052 | 27922 | 12130 (326) | 7 | $-14239.19 | -5.7% |
| **+10¢ (15¢ stop)** | 87666 | 87457 | 209 (128) | 1 | $-32147.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 19:57 | +5 | HYPE | DOWN | 0.67 | open |  |
| 11-25 19:57 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-25 19:56 | +10 stop | ETH | UP | 0.47 | open |  |
| 11-25 19:56 | +5 | ETH | UP | 0.47 | 0.54 | 0.34 |
| 11-25 19:56 | +10 stop | ZEC | UP | 0.67 | 0.51 | -1.94 |
| 11-25 19:56 | +20 | ZEC | UP | 0.67 | open |  |
| 11-25 19:56 | +15 | ZEC | UP | 0.68 | open |  |
| 11-25 19:56 | +10 | ZEC | UP | 0.68 | open |  |
| 11-25 19:56 | +5 | ZEC | UP | 0.67 | open |  |
| 11-25 19:56 | +10 stop | HYPE | UP | 0.50 | 0.34 | -1.98 |
| 11-25 19:56 | +20 | HYPE | UP | 0.49 | open |  |
| 11-25 19:56 | +15 | HYPE | UP | 0.49 | open |  |
| 11-25 19:56 | +10 | HYPE | UP | 0.49 | open |  |
| 11-25 19:56 | +5 | HYPE | UP | 0.49 | 0.56 | 0.36 |
| 11-25 19:56 | +10 stop | SOL | UP | 0.41 | 0.57 | 1.25 |
| 11-25 19:56 | +5 | SOL | UP | 0.39 | 0.57 | 1.45 |
| 11-25 19:56 | +10 stop | XRP | UP | 0.40 | 0.57 | 1.35 |
| 11-25 19:56 | +5 | XRP | UP | 0.44 | 0.57 | 0.94 |
| 11-25 19:55 | +5 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 11-25 19:54 | +10 stop | XRP | DOWN | 0.47 | 0.26 | -2.42 |
| 11-25 19:54 | +20 | XRP | DOWN | 0.47 | 0.69 | 1.87 |
| 11-25 19:54 | +15 | XRP | DOWN | 0.47 | 0.62 | 1.15 |
| 11-25 19:54 | +10 | XRP | DOWN | 0.47 | 0.62 | 1.15 |
| 11-25 19:54 | +5 | XRP | DOWN | 0.47 | 0.56 | 0.54 |
| 11-25 19:54 | +5 | ETH | UP | 0.67 | 0.84 | 1.44 |
| 11-25 19:53 | +5 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 11-25 19:53 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.95 |
| 11-25 19:53 | +5 | BNB | UP | 0.65 | 0.77 | 0.91 |
| 11-25 19:52 | +10 stop | ETH | DOWN | 0.52 | 0.30 | -2.53 |
| 11-25 19:52 | +15 | ETH | DOWN | 0.49 | open |  |
| 11-25 19:52 | +10 | ETH | DOWN | 0.49 | 0.61 | 0.85 |
| 11-25 19:52 | +5 | ETH | DOWN | 0.51 | 0.58 | 0.34 |
| 11-25 19:52 | +10 | BTC | DOWN | 0.50 | open |  |
| 11-25 19:52 | +10 stop | SOL | DOWN | 0.65 | 0.46 | -2.24 |
| 11-25 19:52 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-25 19:52 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 11-25 19:52 | +10 stop | NEAR | DOWN | 0.56 | 0.70 | 1.11 |
| 11-25 19:52 | +15 | NEAR | DOWN | 0.55 | 0.70 | 1.22 |
| 11-25 19:52 | +10 | NEAR | DOWN | 0.55 | 0.70 | 1.20 |
| 11-25 19:52 | +5 | NEAR | DOWN | 0.56 | 0.70 | 1.07 |
