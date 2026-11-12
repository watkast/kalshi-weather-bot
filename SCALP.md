# Range-Scalp Bot

*Updated Thu Nov 12 06:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56767 | 49485 | 7282 (98) | 6 | $-15657.26 | -4.4% |
| **+10¢** | 42418 | 33925 | 8493 (128) | 8 | $-14594.85 | -5.5% |
| **+15¢** | 35562 | 26419 | 9143 (162) | 8 | $-13235.83 | -5.9% |
| **+20¢** | 31675 | 22081 | 9594 (212) | 8 | $-11632.46 | -5.9% |
| **+10¢ (15¢ stop)** | 69224 | 69101 | 123 (73) | 0 | $-25622.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 06:24 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 11-12 06:24 | +5 | ETH | UP | 0.68 | 0.80 | 0.92 |
| 11-12 06:23 | +10 stop | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 11-12 06:23 | +5 | ETH | DOWN | 0.45 | 0.56 | 0.74 |
| 11-12 06:23 | +10 stop | BTC | UP | 0.65 | 0.83 | 1.54 |
| 11-12 06:23 | +5 | HYPE | UP | 0.64 | 0.83 | 1.63 |
| 11-12 06:23 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-12 06:23 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-12 06:22 | +5 | HYPE | DOWN | 0.54 | 0.64 | 0.65 |
| 11-12 06:21 | +10 stop | ETH | DOWN | 0.64 | 0.47 | -2.05 |
| 11-12 06:21 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-12 06:21 | +10 stop | HYPE | DOWN | 0.55 | 0.36 | -2.25 |
| 11-12 06:21 | +15 | HYPE | DOWN | 0.55 | open |  |
| 11-12 06:21 | +10 | HYPE | DOWN | 0.55 | open |  |
| 11-12 06:21 | +5 | HYPE | DOWN | 0.55 | 0.63 | 0.45 |
| 11-12 06:21 | +5 | XRP | DOWN | 0.55 | open |  |
| 11-12 06:21 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.14 |
| 11-12 06:21 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-12 06:21 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-12 06:21 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-12 06:21 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-12 06:19 | +10 stop | DOGE | UP | 0.52 | 0.74 | 1.88 |
| 11-12 06:19 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 11-12 06:19 | +5 | ZEC | DOWN | 0.61 | 0.74 | 0.95 |
| 11-12 06:19 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-12 06:18 | +5 | BNB | UP | 0.66 | 0.75 | 0.60 |
| 11-12 06:18 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-12 06:17 | +10 stop | ZEC | DOWN | 0.55 | 0.74 | 1.58 |
| 11-12 06:17 | +20 | ZEC | DOWN | 0.55 | 0.75 | 1.68 |
| 11-12 06:17 | +15 | ZEC | DOWN | 0.55 | 0.74 | 1.58 |
| 11-12 06:17 | +10 | ZEC | DOWN | 0.54 | 0.74 | 1.68 |
| 11-12 06:17 | +5 | ZEC | DOWN | 0.54 | 0.59 | 0.15 |
| 11-12 06:17 | +10 stop | SOL | DOWN | 0.58 | 0.32 | -2.94 |
| 11-12 06:17 | +20 | SOL | DOWN | 0.58 | open |  |
| 11-12 06:17 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-12 06:17 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-12 06:17 | +5 | SOL | DOWN | 0.58 | open |  |
| 11-12 06:16 | +10 stop | HYPE | UP | 0.52 | 0.30 | -2.52 |
| 11-12 06:16 | +10 stop | BNB | UP | 0.60 | 0.75 | 1.19 |
| 11-12 06:16 | +20 | BNB | UP | 0.60 | 0.85 | 2.24 |
