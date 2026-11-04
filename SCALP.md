# Range-Scalp Bot

*Updated Wed Nov 04 22:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47624 | 41466 | 6158 (73) | 3 | $-13747.18 | -4.6% |
| **+10¢** | 35587 | 28445 | 7142 (98) | 3 | $-12556.14 | -5.6% |
| **+15¢** | 29817 | 22125 | 7692 (126) | 3 | $-11501.16 | -6.1% |
| **+20¢** | 26496 | 18439 | 8057 (166) | 4 | $-10149.70 | -6.1% |
| **+10¢ (15¢ stop)** | 58057 | 57964 | 93 (56) | 0 | $-21593.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 22:34 | +5 | BTC | UP | 0.65 | open |  |
| 11-04 22:32 | +10 stop | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +20 | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +15 | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +10 | ETH | UP | 0.68 | 0.91 | 2.06 |
| 11-04 22:32 | +5 | ETH | UP | 0.68 | 0.76 | 0.51 |
| 11-04 22:32 | +10 stop | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-04 22:32 | +20 | XRP | UP | 0.71 | open |  |
| 11-04 22:32 | +15 | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-04 22:32 | +10 | XRP | UP | 0.71 | 0.86 | 1.26 |
| 11-04 22:32 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 11-04 22:32 | +10 stop | BTC | UP | 0.54 | 0.64 | 0.65 |
| 11-04 22:32 | +20 | BTC | UP | 0.54 | open |  |
| 11-04 22:32 | +15 | BTC | UP | 0.55 | open |  |
| 11-04 22:32 | +10 | BTC | UP | 0.55 | open |  |
| 11-04 22:32 | +5 | BTC | UP | 0.55 | 0.60 | 0.15 |
| 11-04 22:31 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-04 22:31 | +10 stop | HYPE | DOWN | 0.58 | 0.33 | -2.84 |
| 11-04 22:31 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-04 22:31 | +10 stop | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +20 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +15 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +10 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 11-04 22:31 | +5 | BNB | UP | 0.65 | 0.70 | 0.19 |
| 11-04 22:31 | +10 stop | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-04 22:31 | +20 | ZEC | UP | 0.70 | 0.93 | 2.13 |
| 11-04 22:31 | +15 | ZEC | UP | 0.70 | 0.93 | 2.13 |
| 11-04 22:31 | +10 | ZEC | UP | 0.70 | 0.83 | 1.05 |
| 11-04 22:31 | +5 | ZEC | UP | 0.70 | 0.78 | 0.52 |
| 11-04 22:30 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 11-04 22:30 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:30 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:30 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:30 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-04 22:28 | +10 stop | ZEC | DOWN | 0.67 | 0.52 | -1.84 |
| 11-04 22:26 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 11-04 22:26 | +20 | HYPE | UP | 0.66 | 0.88 | 1.96 |
