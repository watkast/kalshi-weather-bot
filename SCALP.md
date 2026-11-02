# Range-Scalp Bot

*Updated Mon Nov 02 12:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44870 | 39073 | 5797 (66) | 0 | $-12966.49 | -4.6% |
| **+10¢** | 33492 | 26775 | 6717 (87) | 0 | $-11834.02 | -5.6% |
| **+15¢** | 28017 | 20788 | 7229 (114) | 0 | $-10886.86 | -6.2% |
| **+20¢** | 24891 | 17323 | 7568 (149) | 0 | $-9616.01 | -6.2% |
| **+10¢ (15¢ stop)** | 54760 | 54673 | 87 (51) | 0 | $-20703.79 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 12:33 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 12:33 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 11-02 12:33 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 12:33 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 12:33 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 11-02 12:31 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-02 12:31 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-02 12:31 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-02 12:31 | +20 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 11-02 12:31 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 11-02 12:31 | +10 | BNB | DOWN | 0.63 | 0.75 | 0.89 |
| 11-02 12:31 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 11-02 12:31 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 11-02 12:31 | +20 | HYPE | DOWN | 0.63 | 0.85 | 1.90 |
| 11-02 12:31 | +15 | HYPE | DOWN | 0.63 | 0.85 | 1.90 |
| 11-02 12:31 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 11-02 12:31 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.34 |
| 11-02 12:28 | +10 stop | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 11-02 12:28 | +5 | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 11-02 12:28 | +10 stop | XRP | UP | 0.52 | 0.63 | 0.75 |
| 11-02 12:28 | +10 stop | SOL | DOWN | 0.67 | 0.91 | 2.20 |
| 11-02 12:28 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 11-02 12:27 | +10 stop | BTC | UP | 0.71 | 0.51 | -2.33 |
| 11-02 12:26 | +10 stop | XRP | DOWN | 0.61 | 0.36 | -2.84 |
| 11-02 12:26 | +10 | XRP | DOWN | 0.59 | 0.95 | 3.36 |
| 11-02 12:26 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 11-02 12:26 | +10 stop | BTC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-02 12:24 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-02 12:24 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 11-02 12:24 | +10 stop | NEAR | DOWN | 0.60 | 0.76 | 1.30 |
| 11-02 12:24 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 11-02 12:24 | +5 | ETH | DOWN | 0.61 | 0.69 | 0.48 |
| 11-02 12:24 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-02 12:23 | +5 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-02 12:23 | +10 stop | BTC | UP | 0.59 | 0.37 | -2.54 |
| 11-02 12:23 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-02 12:22 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.36 |
| 11-02 12:22 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 12:22 | +10 stop | DOGE | DOWN | 0.68 | 0.44 | -2.74 |
| 11-02 12:22 | +10 stop | SOL | DOWN | 0.70 | 0.87 | 1.47 |
