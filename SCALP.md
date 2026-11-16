# Range-Scalp Bot

*Updated Mon Nov 16 02:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61545 | 53711 | 7834 (115) | 8 | $-16518.52 | -4.3% |
| **+10¢** | 45972 | 36791 | 9181 (156) | 9 | $-15483.55 | -5.4% |
| **+15¢** | 38519 | 28613 | 9906 (195) | 9 | $-14124.35 | -5.8% |
| **+20¢** | 34336 | 23945 | 10391 (247) | 9 | $-12368.71 | -5.7% |
| **+10¢ (15¢ stop)** | 74910 | 74756 | 154 (90) | 0 | $-27519.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 02:21 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-16 02:20 | +10 stop | XRP | UP | 0.67 | 0.84 | 1.44 |
| 11-16 02:20 | +5 | XRP | UP | 0.67 | 0.74 | 0.40 |
| 11-16 02:20 | +5 | XRP | UP | 0.53 | 0.58 | 0.14 |
| 11-16 02:18 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-16 02:18 | +10 stop | XRP | UP | 0.55 | 0.68 | 0.96 |
| 11-16 02:18 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-16 02:18 | +5 | XRP | UP | 0.58 | 0.63 | 0.15 |
| 11-16 02:18 | +10 stop | ZEC | UP | 0.69 | 0.51 | -2.13 |
| 11-16 02:18 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 11-16 02:17 | +5 | XRP | DOWN | 0.45 | 0.58 | 0.94 |
| 11-16 02:17 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-16 02:17 | +10 stop | NEAR | DOWN | 0.64 | 0.47 | -2.05 |
| 11-16 02:17 | +20 | NEAR | DOWN | 0.64 | open |  |
| 11-16 02:17 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-16 02:17 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-16 02:17 | +5 | NEAR | DOWN | 0.64 | open |  |
| 11-16 02:17 | +10 stop | ZEC | DOWN | 0.69 | 0.51 | -2.13 |
| 11-16 02:17 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-16 02:17 | +15 | ZEC | DOWN | 0.69 | open |  |
| 11-16 02:17 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-16 02:17 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-16 02:16 | +10 stop | ETH | DOWN | 0.65 | 0.40 | -2.83 |
| 11-16 02:16 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-16 02:16 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-16 02:16 | +10 stop | BNB | DOWN | 0.64 | 0.43 | -2.45 |
| 11-16 02:16 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-16 02:16 | +15 | BNB | DOWN | 0.61 | open |  |
| 11-16 02:16 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-16 02:16 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-16 02:16 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.95 |
| 11-16 02:16 | +20 | HYPE | DOWN | 0.62 | open |  |
| 11-16 02:16 | +15 | HYPE | DOWN | 0.62 | open |  |
| 11-16 02:16 | +10 | HYPE | DOWN | 0.62 | open |  |
| 11-16 02:16 | +5 | HYPE | DOWN | 0.62 | open |  |
| 11-16 02:16 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.05 |
| 11-16 02:16 | +20 | SOL | DOWN | 0.59 | open |  |
| 11-16 02:16 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-16 02:16 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-16 02:16 | +5 | SOL | DOWN | 0.59 | open |  |
